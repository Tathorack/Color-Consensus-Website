#!venv_flask/bin/python
import os
os.environ['FLASKAPP_ENV'] = 'lights'
from flaskfiles import app
app.run(host='0.0.0.0')
