import logging

from colorutils import rgb_to_hsv
from qhue import Bridge, QhueException


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


def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)


class HueLightControler(object):
    """docstring for HueLightControler."""
    def __init__(self, brige_ip, user):
        self.bridge = Bridge(brige_ip, user)
        self.lights = self.bridge.lights()

    def set_hue_color(self, lightid, red, green, blue):
        hsv = rgb_to_hsv((red, green, blue))
        self.bridge.lights[lightid].state(
            on=True,
            hue=round((hsv[0]*65535)/360),
            sat=round(hsv[1]*255),
            bri=round(hsv[2]*255)
            )
