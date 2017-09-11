#!venv_flask/bin/python
# coding=UTF-8
import argparse
import csv
import re
import time
import os

from datetime import datetime

from flask import Flask
app = Flask(__name__)

from flaskfiles.database import db, Searches
config = os.environ.get("FLASKAPP_CONFIG")
if config is not None:
    app.config.from_object(config)
else:
    app.config.from_object('flaskfiles.settings.Config')

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', help='Source log file to parse: Default ./flask.log', default='./flask.log', required=False)
args = parser.parse_args()

with open(args.source, 'r') as logfile:
    for line in logfile:
        try:
            if re.search('search:', line):
                dt = datetime.fromtimestamp(time.mktime(time.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')))
                retime = re.search(' ([0-9]+\.[0-9][0-9][0-9]) seconds', line)
                line = line.split('search:')[1]
                search = line.split('R:')[0].strip()
                red = int(line.split('R:')[1].split('G:')[0].strip())
                green = int(line.split('G:')[1].split('B:')[0].strip())
                blue = int(line.split('B:')[1].split('HEX:')[0].strip())
                current = Searches(
                    search,
                    'google',
                    red,
                    green,
                    blue,
                    float(retime.group().strip(' seconds')),
                    timestamp=dt)
                db.session.add(current)
                db.session.commit()
        except Exception as e:
            print(e)
