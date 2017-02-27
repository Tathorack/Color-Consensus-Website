from time import time
import logging

from flask import render_template, request, jsonify, redirect

from colorutils import rgb_to_hsv
import imagecolor
from qhue import Bridge, QhueException
import searchcolor

from flaskfiles import app

if app.config['SEARCH'] == 'bing':
    from flaskfiles.extensions.api_keys import BingKeyLocker
    BKL = BingKeyLocker()
else:
    from flaskfiles.extensions.api_keys import GoogleKeyLocker
    GKL = GoogleKeyLocker()

if app.config['LIGHTS'] == True:
    BRIDGE_IP='192.168.1.29'
    HUE_USER='3DQZXO2BnrAepp95yjIiyV0CZF9g5d78332az30f'
    bridge = Bridge(BRIDGE_IP, HUE_USER)
    lights = bridge.lights()

def set_hue_color(lightid, red, green, blue):
        hsv = rgb_to_hsv((red, green, blue))
        lightid='1'
        hue = round((hsv[0]*65535)/360)
        sat = round(hsv[1]*255)
        bri = round(hsv[2]*255)
        app.logger.info('Hue %0.3f=%d Sat %0.3f=%d Val %0.3f=%d', hsv[0], hue, hsv[1], sat,hsv[2], bri)
        bridge.lights[lightid].state(on=True, bri=bri, hue=hue, sat=sat)

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
    red = color.get('red')
    green = color.get('green')
    blue = color.get('blue')
    t1 = time() - t0
    app.logger.info('Search Average response took %0.3f seconds with %s - search: %s R:%d G:%d B:%d HEX:%s', t1, app.config['SEARCH'], search, red, green, blue, result)
    if app.config['LIGHTS'] == True:
        set_hue_color('1', red, green, blue)
    return jsonify(result=result, red=red, green=green, blue=blue)
