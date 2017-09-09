import os
from time import time
import logging

from flask import render_template, request, jsonify, redirect

from colorutils import rgb_to_hsv
import imagecolor
from qhue import Bridge, QhueException
import searchcolor
from searchcolor import ZeroResultsException

from flaskfiles import app
from flaskfiles.utilities import HueLightControler, rgb_to_hex

api = os.environ.get("GOOGLE_SEARCH_API")
cse = os.environ.get("GOOGLE_SEARCH_CSE")
display = app.config['DISPLAY_MODE']

if app.config['LIGHTS'] is True:
    BRIDGE_IP = os.environ.get('BRIDGE_IP')
    HUE_USER = os.environ.get('HUE_USER')
    lightcontrol = HueLightControler(BRIDGE_IP, HUE_USER)


@app.route('/')
def redirec_to_display():
    if display == 'thesis-install':
        return render_template('thesis_installation.html')
    elif display == 'thesis-web':
        return render_template('thesis_web.html')
    else:
        return render_template('home.html')

@app.route('/index/')
def index():
    return render_template("home.html")

@app.route('/single_average/')
def single_average():
    return render_template('single_average.html')

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
    app.logger.info('Image Average response took %0.3f seconds - R:%d, G:%d, B:%d, HEX:%s',processing_time, red, green, blue, result)
    return jsonify(result=result, red=red, green=green, blue=blue)

@app.route('/search_average/')
def search_average():
    return render_template('search_average.html')

@app.route('/thesis_installation/')
def thesis_installation():
    return render_template('thesis_installation.html')

@app.route('/thesis_web/')
def thesis_web():
    return render_template('thesis_web.html')

@app.route('/search_average/_search_single', methods=['POST'])
def average_search_images():
    try:
        t0 = time()
        search = request.get_json()['search']
        app.logger.debug(search)
        color = searchcolor.google_average(search, 10, api, cse, max_threads=3, timeout=3, max_size=2)
        red = color.get('red')
        green = color.get('green')
        blue = color.get('blue')
        hexcolor = rgb_to_hex(red, green, blue)
        t1 = time() - t0
        app.logger.info('Search Average response took %0.3f seconds with %s - search: %s R:%d G:%d B:%d HEX:%s', t1, app.config['SEARCH'], search, red, green, blue, hexcolor)
        if app.config['LIGHTS'] == True:
            lightcontrol.set_hue_color('1', red, green, blue)
        result = 'Success'
        return(jsonify(result=result, hexcolor=hexcolor, red=red, green=green, blue=blue))
    except ZeroResultsException as e:
        app.logger.warning('Exception: %s', e)
        app.logger.debug('Traceback:', exc_info=True)
        result = 'No results'
        return(jsonify(result=result))
    except Exception as e:
        app.logger.warning('Exception: %s', e)
        app.logger.debug('Traceback:', exc_info=True)
        result = 'An error occured'
        return(jsonify(result=result))
