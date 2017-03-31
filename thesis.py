#!venv_flask/bin/python
import os
os.environ['FLASKAPP_ENV'] = 'thesis'
from flaskfiles import app
app.run()
