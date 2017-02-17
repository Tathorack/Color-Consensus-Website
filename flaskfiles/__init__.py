import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

app = Flask(__name__)

from flaskfiles import views



file_handler = RotatingFileHandler('logs/flask.log', maxBytes=1024 * 1024 * 100, backupCount=20)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Flask logger configured')

colorlogger = logging.getLogger('imagecolor')
colorlogger.addHandler(file_handler)
colorlogger.setLevel(logging.WARNING)
colorlogger.info('imagecolor logger configured')
colorlogger.info('imagecolor v%s',views.imagecolor.__version__)

searchlogger = logging.getLogger('searchcolor')
searchlogger.addHandler(file_handler)
searchlogger.setLevel(logging.WARNING)
searchlogger.info('searchcolor logger configured')
searchlogger.info('searchcolor v%s',views.searchcolor.__version__)
