import logging
from logging.handlers import RotatingFileHandler
import os

from flask import Flask

app = Flask(__name__)

env = os.environ.get("FLASKAPP_ENV")
log = os.environ.get("FLASKAPP_LOG")

if env == 'dev':
    app.config.from_object('flaskfiles.settings.DevConfig')
elif env == 'lights':
    app.config.from_object('flaskfiles.settings.LightsConfig')
elif env == 'thesis':
    app.config.from_object('flaskfiles.settings.ThesisConfig')
elif env == 'colors':
    app.config.from_object('flaskfiles.settings.ColorsSiteConfig')
elif env == 'test':
    app.config.from_object('flaskfiles.settings.TestConfig')
else:
    app.config.from_object('flaskfiles.settings.Config')

if log == None:
    log = 'flask.log'

from flaskfiles import views

def logging_config(log, configvalue):
    if configvalue == 'CRITICAL':
        log.setLevel(logging.CRITICAL)
    elif configvalue == 'ERROR':
        log.setLevel(logging.ERROR)
    elif configvalue == 'WARNING':
        log.setLevel(logging.WARNING)
    elif configvalue == 'INFO':
        log.setLevel(logging.INFO)
    elif configvalue == 'DEBUG':
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)

file_handler = RotatingFileHandler(log, maxBytes=1024 * 1024 * 100, backupCount=20)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)
logging_config(app.logger, app.config['FLASK_LOGGING'])
app.logger.info('Flask logger configured')
app.logger.info('Config used %s', env)

colorlogger = logging.getLogger('imagecolor')
colorlogger.addHandler(file_handler)
logging_config(colorlogger, app.config['LIB_LOGGING'])
colorlogger.info('imagecolor logger configured')
colorlogger.info('imagecolor v%s',views.imagecolor.__version__)

searchlogger = logging.getLogger('searchcolor')
searchlogger.addHandler(file_handler)
logging_config(searchlogger, app.config['LIB_LOGGING'])
searchlogger.info('searchcolor logger configured')
searchlogger.info('searchcolor v%s',views.searchcolor.__version__)
