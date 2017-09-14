# stdlib imports
import logging
import os
from time import time
# package imports
from flask import render_template, request, jsonify, redirect
import imagecolor
import searchcolor
# local imports
from flaskfiles import app
from flaskfiles.database import db, Searches
from flaskfiles.utilities import HueLightControler, rgb_to_hex, table_display

# get values from environment
api = os.environ["GOOGLE_SEARCH_API"]
cse = os.environ["GOOGLE_SEARCH_CSE"]

# if lights are enabled create a lightcontroller
if app.config['LIGHTS'] is True:
    BRIDGE_IP = os.environ.get('BRIDGE_IP')
    HUE_USER = os.environ.get('HUE_USER')
    lightcontrol = HueLightControler(BRIDGE_IP, HUE_USER)


@app.route('/')
def redirec_to_display():
    if app.config['DISPLAY_MODE'] == 'thesis-install':
        return render_template('thesis_installation.html')
    elif app.config['DISPLAY_MODE'] == 'thesis-web':
        return render_template('thesis_web.html')
    else:
        return render_template('home.html')


@app.route('/index/')
def index():
    return render_template("home.html")


@app.route('/history/')
def history():
    searches = [table_display(
        search.search, search.red,
        search.green, search.blue)
                for search in
                Searches.query.order_by(Searches.timestamp.desc()).all()]
    return render_template('history.html',
                           searches=searches, count=len(searches))


@app.route('/single_average/')
def single_average():
    return render_template('single_average.html')


@app.route('/search_average/')
def search_average():
    return render_template('search_average.html')


@app.route('/thesis_installation/')
def thesis_installation():
    return render_template('thesis_installation.html')


@app.route('/thesis_web/')
def thesis_web():
    return render_template('thesis_web.html')


# POST functions that take a json request and return a response
@app.route('/search_average/_search_single', methods=['POST'])
def average_search_images():
    try:
        response_t = time()
        search = request.get_json()['search']
        app.logger.debug(search)
        color = searchcolor.google_average(
            search, 10, api, cse, max_threads=3, timeout=3, max_size=2)
        response_t = time() - response_t
        app.logger.info('Search Average response took %0.3f seconds with %s'
                        ' - search: %s R:%d G:%d B:%d HEX:%s',
                        response_t,
                        app.config['SEARCH'],
                        search,
                        color['red'],
                        color['green'],
                        color['blue'],
                        rgb_to_hex(
                            color['red'],
                            color['green'],
                            color['blue']))
        current = Searches(
            search,
            app.config['SEARCH'],
            color['red'],
            color['green'],
            color['blue'],
            response_t)
        db.session.add(current)
        db.session.commit()
        if app.config['LIGHTS'] is True:
            lightcontrol.set_hue_color(
                '1',
                color['red'],
                color['green'],
                color['blue'])
        return jsonify({'result': 'success',
                        'search': search,
                        'hex': rgb_to_hex(
                            color['red'],
                            color['green'],
                            color['blue']),
                        'red': color['red'],
                        'green': color['green'],
                        'blue': color['blue']})
    except searchcolor.ZeroResultsException as e:
        app.logger.warning('Exception: %s', e)
        app.logger.debug('Traceback:', exc_info=True)
        return(jsonify(result='no results'))
    except Exception as e:
        app.logger.warning('Exception: %s', e)
        app.logger.debug('Traceback:', exc_info=True)
        return(jsonify(result='an error occured'))


@app.route('/single_average/_average_single', methods=['POST'])
def average_upload_image():
    start = time()
    result = '#'
    color = ['upload', 255, 255, 255]
    f = request.files['file']
    color = imagecolor.average(f, name='upload')
    red = color.get('red')
    green = color.get('green')
    blue = color.get('blue')
    result = rgb_to_hex(red, green, blue)
    processing_time = time() - start
    app.logger.info('Image Average response took %0.3f seconds - '
                    'R:%d, G:%d, B:%d, HEX:%s',
                    processing_time, red, green, blue, result)
    return jsonify(result=result, red=red, green=green, blue=blue)
