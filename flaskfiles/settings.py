class Config(object):
    ENV = 'prod'
    DEBUG = False
    FLASK_LOGGING = 'INFO'
    LIB_LOGGING = 'WARNING'
    LIGHTS = False
    SEARCH = 'google'
    DISPLAY_MODE = 'default'

class LightsConfig(Config):
    ENV = 'lights'
    DEBUG = False
    LIGHTS = True

class ThesisConfig(Config):
    ENV = 'thesis'
    DEBUG = False
    LIGHTS = True
    DISPLAY_MODE = 'thesis'

class ColorsSiteConfig(Config):
    ENV = 'colors'
    DEBUG = False
    DISPLAY_MODE = 'colors'

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    LIB_LOGGING = 'DEBUG'

class TestConfig(DevConfig):
    ENV = 'test'
    DEBUG = True
    LIB_LOGGING = 'DEBUG'
    SEARCH = 'bing'
