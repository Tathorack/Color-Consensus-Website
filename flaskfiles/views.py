from flaskfiles import app
from flask import render_template, request, jsonify, redirect
import image_colors
import image_search_colors
from flaskfiles.extensions.api_keys import GoogleKeyLocker
import pprint
GKL = GoogleKeyLocker()

def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)

ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']

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
    color = image_colors.average_single_image(f, name='upload')
    result = rgb_to_hex(color[1],color[2],color[3])
    return jsonify(result=result, color=color)

@app.route('/search_average/')
def search_average():
    """Test File Upload."""
    return render_template('search_average.html')

@app.route('/search_average/_search_single', methods=['POST'])
def average_search_images():
    result = '#'
    color = ['search', " ", " ", " "]
    search = request.get_json()['search']
    color = image_search_colors.google_average(search, 20, GKL.api(), GKL.cse())
    result = rgb_to_hex(color[1],color[2],color[3])
    return jsonify(result=result, color=color)
