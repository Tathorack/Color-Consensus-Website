import logging


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
