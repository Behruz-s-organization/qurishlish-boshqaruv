import os
from pathlib import Path

from config.env import env


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(asctime)s %(name)s %(levelname)s %(message)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(Path(__file__).resolve().parent.parent, 'logs/django.log'),
            'maxBytes': 1024 * 1024 * 15, 
            'backupCount': 10,
            'formatter': 'verbose',
        },
        'loki': {
            'level': 'INFO',
            'class': 'logging_loki.LokiHandler',
            'url': env.str('LOKI_URL', 'http://localhost:3100/loki/api/v1/push'),
            'tags': {
                'application': 'django-app',
                'environment': env.str('ENVIRONMENT', 'development')
            },
            'version': '1',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file', 'loki'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'file', 'loki'],
            'level': 'ERROR',
            'propagate': False,
        },
        'accounts': {  
            'handlers': ['console', 'file', 'loki'],
            'level': 'INFO',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console', 'file', 'loki'],
        'level': 'INFO',
    }
}