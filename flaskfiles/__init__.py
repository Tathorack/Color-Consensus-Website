
from flask import Flask
app = Flask(__name__)

from flaskfiles import views

if app.debug is not True:
    import logging
    from logging.handlers import RotatingFileHandler
    logger = logging.getLogger(__name__)
    file_handler = RotatingFileHandler('flask.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

app.logger.info('app.logger')
