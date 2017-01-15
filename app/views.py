from app import app
from flask import render_template, request, jsonify, redirect
from app.extensions.image_color_average import imgavg as ia
import pprint

def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)

ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']

@app.route('/')
@app.route('/index/')
def index():
    return render_template("home.html")

@app.route('/single_average/')
def upload():
    """Test File Upload."""
    return render_template('single_average.html')

@app.route('/single_average/_average_single', methods=['POST','GET'])
def upload_test():
    result = '#'
    color = ['upload', 255, 255, 255]
    f = request.files['file']
    color = ia.avg_single_img(f, name='upload')
    result = rgb_to_hex(color[1],color[2],color[3])
    return jsonify(result=result, color=color)
