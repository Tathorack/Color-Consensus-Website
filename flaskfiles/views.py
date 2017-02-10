from flask import render_template, request, jsonify, redirect

import imagecolor
import searchcolor

from flaskfiles import app
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
    result = '#'
    color = ['upload', 255, 255, 255]
    f = request.files['file']
    color = imagecolor.average(f, name='upload')
    red = color.get('red')
    green = color.get('green')
    blue = color.get('blue')
    result = rgb_to_hex(red, green, blue)
    app.logger.info('Image Average: R:%d, G:%d, B:%d, HEX:%s', red, green, blue, result)

    return jsonify(result=result, red=red, green=green, blue=blue)

@app.route('/search_average/')
def search_average():
    """Test File Upload."""
    return render_template('search_average.html')

@app.route('/search_average/_search_single', methods=['POST'])
def average_search_images():
    result = '#fff'
    color = {'red':-1, 'green':-1, 'blue':-1}
    search = request.get_json()['search']
    color = searchcolor.google_average(search, 20, GKL.api(), GKL.cse())
    red = color.get('red')
    green = color.get('green')
    blue = color.get('blue')
    result = rgb_to_hex(red, green, blue)
    app.logger.info('Search Average | Search: %s R:%d G:%d B:%d HEX:%s',search, red, green, blue, result)
    return jsonify(result=result, red=red, green=green, blue=blue)
