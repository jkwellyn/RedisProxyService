class Config(object):
    DEBUG = False

class DevelopmentConfig(Config):
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    TTL = 360
    CAPACITY = 10
    HOST = ""
    PORT = ""
    DEBUG = True
