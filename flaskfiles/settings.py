class Config(object):
    ENV = 'prod'
    DEBUG = False
    FLASK_LOGGING = 'INFO'
    LIB_LOGGING = 'WARNING'
    LIGHTS = False
    SEARCH = 'google'
    DISPLAY_MODE = 'default'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////'
    'Users/rhyshansen/programming/source/project_website/thesis.db'


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
    ENV = 'thesis-web'
    DEBUG = False
    SEARCH = 'google-limited'
    DISPLAY_MODE = 'thesis-web'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    LIB_LOGGING = 'DEBUG'
