from time import time
import logging

from flask import render_template, request, jsonify, redirect

import imagecolor
import searchcolor

from flaskfiles import app

if app.config['SEARCH'] == 'bing':
    from flaskfiles.extensions.api_keys import BingKeyLocker
    BKL = BingKeyLocker()
else:
    from flaskfiles.extensions.api_keys import GoogleKeyLocker
    GKL = GoogleKeyLocker()

def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)

@app.route('/')
@app.route('/index/')
def index():
    return render_template("home.html")

@app.route('/single_average/')
def single_average():
    """Test File Upload."""
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
    """Test File Upload."""
    return render_template('search_average.html')

@app.route('/search_average/_search_single', methods=['POST'])
def average_search_images():
    t0 = time()
    result = '#fff'
    color = {'red':-1, 'green':-1, 'blue':-1}
    search = request.get_json()['search']
    if app.config['SEARCH'] == 'bing':
        color = searchcolor.bing_average(search, 10, BKL.api(), max_threads=3, timeout=3, max_size=2)
    else:
        color = searchcolor.google_average(search, 10, GKL.api(), GKL.cse(), max_threads=3, timeout=3, max_size=2)
    result = rgb_to_hex(color.get('red'), color.get('green'), color.get('blue'))
    t1 = time() - t0
    app.logger.info('Search Average response took %0.3f seconds with %s - search: %s R:%d G:%d B:%d HEX:%s', t1, app.config['SEARCH'], search, red, green, blue, result)
    return jsonify(result=result, red=color.get('red'), green=color.get('green'), blue=color.get('blue'))
