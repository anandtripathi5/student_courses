from webargs import fields, ValidationError
from webargs.djangoparser import parser


def parsing(request, validator):
    try:
        args = parser.parse(validator, request)
    except ValidationError as err:
        raise ValueError(err.message)
    return args
