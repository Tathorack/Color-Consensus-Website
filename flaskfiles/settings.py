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

class ThesisInstallConfig(Config):
    ENV = 'thesis-install'
    DEBUG = False
    LIGHTS = True
    DISPLAY_MODE = 'thesis-install'

class ThesisWebConfig(Config):
    ENV = 'thesis_web'
    DEBUG = False
    SEARCH = 'limited'
    DISPLAY_MODE = 'thesis-web'

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    LIB_LOGGING = 'DEBUG'

class TestConfig(DevConfig):
    ENV = 'test'
    DEBUG = True
    LIB_LOGGING = 'DEBUG'
    SEARCH = 'bing'
