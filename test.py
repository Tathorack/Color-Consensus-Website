#!venv_flask/bin/python
import os
os.environ['FLASKAPP_ENV'] = 'test'
from flaskfiles import app
app.run(host='0.0.0.0', debug=True)
