import json
from functools import wraps

from django.db import IntegrityError
from django.http.response import HttpResponse
from jwt import ExpiredSignatureError, DecodeError
from rest_framework.exceptions import AuthenticationFailed
from webargs.core import ValidationError
from logger import logger


class AuthorizationFailedError(Exception):
    pass


class AlreadyExists(Exception):
    pass


def handle_exceptions(fn):
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        try:
            return fn(self, *args, **kwargs)
        except ValueError as val_err:
            logger.error(val_err.message)
            return HttpResponse(
                json.dumps({'message': val_err.message}),
                status=400,
                content_type="application/json"
            )
        except KeyError as key_err:
            logger.error(key_err.message)
            return HttpResponse(
                json.dumps({'message': key_err.message}),
                status=400,
                content_type="application/json"
            )
        except IOError as io_err:
            logger.error(io_err.message)
            return HttpResponse(
                json.dumps({'message': io_err.message}),
                status=302,
                content_type="application/json"
            )
        except IntegrityError as io_err:
            logger.error(io_err[1])
            return HttpResponse(
                json.dumps({'message': io_err[1]}),
                status=400,
                content_type="application/json"
            )
        except AuthorizationFailedError as auth_err:
            logger.error(auth_err.message)
            return HttpResponse(
                json.dumps({'message': auth_err.message}),
                status=403,
                content_type="application/json"
            )
        except AuthenticationFailed as auth_err:
            logger.error(auth_err.message)
            return HttpResponse(
                json.dumps({'message': auth_err.message}),
                status=401,
                content_type="application/json"
            )
        except DecodeError as auth_err:
            logger.error(auth_err.message)
            return HttpResponse(
                json.dumps({'message': auth_err.message}),
                status=401,
                content_type="application/json"
            )
        except AlreadyExists as err:
            logger.error(err.message)
            return HttpResponse(
                json.dumps({'message': err.message}),
                status=409,
                content_type="application/json"
            )
        except ExpiredSignatureError as es_err:
            logger.error(es_err.message)
            return HttpResponse(
                json.dumps({'message': es_err.message}),
                status=401,
                content_type="application/json"
            )
        except ValidationError as es_err:
            logger.error(es_err.message)
            return HttpResponse(
                json.dumps({'message': es_err.message}),
                status=422,
                content_type="application/json"
            )
        except Exception as exc:
            logger.error(exc.message)
            return HttpResponse(
                json.dumps({'message': exc.message}),
                status=500,
                content_type="application/json"
            )
    return wrapper
