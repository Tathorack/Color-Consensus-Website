from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")

@app.route('/upload/')
def upload():
    """Test File Upload."""
    return render_template('users/upload.html')

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")

@app.route('/upload/bounce', methods=["POST"])
def transform_view():
    file = request.files['data_file']
    if not file:
        return "No file"
    file_contents = file.stream.read().decode("utf-8")
    result = transform(file_contents)
    response = make_response(result)
    response.headers["Content-Disposition"] = "attachment; filename=result.csv"
    return response
