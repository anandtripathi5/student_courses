# Logging settings for django projects, works with django 1.5+
# If DEBUG=True, all logs (including django logs) will be
# written to console and to debug_file.
# If DEBUG=False, logs with level INFO or higher will be
# saved to production_file.
# Logging usage:

import logging.config
import logging

import sys

LOGGING_CONF = dict(
    version=1,
    disable_existing_loggers=False,
    formatters={
        'compact': {
            'format': '%(process)d - %(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - [%(levelname)s] - %(message)s'
        },
        'err_report': {'format': '%(asctime)s\n%(message)s'}
    },
    handlers={
        "student_course": {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'compact',
            'level': 'DEBUG'
        }
    },
    loggers={
        "student_course": {
            'handlers': ["student_course"],
            'level': 'DEBUG',
            'propagate': False
        },
        'crash': {
            'handlers': ["student_course"],
            'level': 'ERROR',
            'propagate': False
        },
    }
)
logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger("student_course")
logger.info("Log this message")