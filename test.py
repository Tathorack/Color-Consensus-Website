#!venv_flask/bin/python
import os
import argparse


def validate_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', help='Config to use', type=str,
                    choices=['Lights', 'ThesisWeb', 'ThesisInstall'],
                    default='')
parser.add_argument('-a', '--host', help='Host IP address: Default 127.0.0.1',
                    default='127.0.0.1', required=False)
parser.add_argument('-p', '--port', help='Host port: Default 5000', type=int,
                    default=5000, required=False)
parser.add_argument('-d', '--debug', help='Force debuging on', default=False,
                    action='store_true')
args = parser.parse_args()

if validate_ip(args.host) is False:
    print("Non valid IP address")
    exit()
os.environ['FLASKAPP_CONFIG'] = 'flaskfiles.settings.{}Config'.format(
    args.config)

from flaskfiles import app
app.run(host=args.host, port=args.port, debug=args.debug)
