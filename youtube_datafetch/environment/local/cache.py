CACHE_BACKEND = 'django_redis.cache.RedisCache'
CACHE_LOCATION = 'redis://127.0.0.1:6379/1'

CACHES = {
    'default': {
        'BACKEND': CACHE_BACKEND,
        'LOCATION': CACHE_LOCATION,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'MAX_ENTRIES': 5000,
        },
    },
}

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': '',
        'DEFAULT_TIMEOUT': 360,
    },
    'DEFAULT_RESULT_TTL': 5000,
}
