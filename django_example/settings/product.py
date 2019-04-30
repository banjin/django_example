# coding:utf-8

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_example',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

REDIS_URL = '127.0.0.1:6379'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'TIMEOUT': 300,
        'OPTIONS': {
            'PASSWORD': '',
            'CLIENT_CLAS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser'

        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool'
    }
}

# 关闭浏览器时候设置session为过期 , 需要定时执行 python manage.py clearsessions,手动删除过期数据
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# 配置邮件服务器
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_PASSWORD = 'password' # 客户端授权码
EMAIL_HOST_USER = '' # 邮箱用户名
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER


LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
            'format': '%(levelname)s [%(asctime)s] %(funcName)s %(message)s'
            },
        },
        'filters': {
		    'require_debug_false': {
			    '()': 'django.utils.log.RequireDebugFalse',
		    },
		    'require_debug_true': {
			    '()': 'django.utils.log.RequireDebugTrue',
		    },
	    },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'console_debug_false': {
			    'level': 'ERROR',
			    'filters': ['require_debug_false'],
			    'class': 'logging.StreamHandler',
		    },
            'django.server': {
			    'level': 'INFO',
			    'class': 'logging.StreamHandler',
			    'formatter': 'simple',
		    },
            # 'file': {
            #     'class': 'logging.handlers.RotatingFileHandler',
            #     'formatter': 'simple',
            #     'filename': '/var/www/logs/ibiddjango.log',
            #     'maxBytes': 1024000,
            #     'backupCount': 3,
            # },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console','console_debug_false','mail_admins'],
                'propagate': True,
                'level': 'DEBUG',
            },
            'django.server': {
			    'handlers': ['django.server'],
			    'level': 'INFO',
			    'propagate': False,
		    }
        }
}
