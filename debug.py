#!venv_flask/bin/python
import os
os.environ['FLASKAPP_ENV'] = 'dev'
from flaskfiles import app
app.run(debug=True)
