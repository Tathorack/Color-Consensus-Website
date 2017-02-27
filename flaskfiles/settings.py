class Config(object):
    ENV = 'prod'
    DEBUG = False
    FLASK_LOGGING = 'INFO'
    LIB_LOGGING = 'WARNING'
    LIGHTS = False
    SEARCH = 'google'

class LightsConfig(Config):
    ENV = 'lights'
    DEBUG = False
    LIGHTS = True

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    LIB_LOGGING = 'DEBUG'

class TestConfig(DevConfig):
    ENV = 'test'
    DEBUG = True
    LIB_LOGGING = 'DEBUG'
    SEARCH = 'bing'
