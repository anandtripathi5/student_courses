import json
from functools import wraps

from django.http.response import HttpResponse
from marshmallow import fields
from rest_framework import status
from django.views.generic import View
from webargs.djangoparser import use_kwargs

from course_app.functionality.student import register_student
from course_app.utils.resource_exception import handle_exceptions

student_signup_request = dict(
    user_name=fields.Str(required=True),
    password=fields.Str(required=True),
    email=fields.Str(required=True)
)


class StudentSignup(View):

    @handle_exceptions
    @use_kwargs(student_signup_request)
    def post(self, *args, **kwargs):
        jwt_token = register_student(**kwargs)
        return HttpResponse(
            json.dumps(dict(token=jwt_token)),
            status=status.HTTP_201_CREATED,
            content_type="application/json"
        )
