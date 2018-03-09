import json
from django.http.response import HttpResponse
from django.views.generic.base import View
from marshmallow import fields
from webargs.djangoparser import use_kwargs

from course_app.functionality.student import login_functionality
from course_app.utils.resource_exception import handle_exceptions


student_login_request = dict(
    user_name=fields.Str(required=True),
    password=fields.Str(required=True)
)


class Login(View):

    @handle_exceptions
    @use_kwargs(student_login_request)
    def post(self, request, **kwargs):
        jwt_token = login_functionality(request, **kwargs)
        return HttpResponse(
            json.dumps(jwt_token),
            status=200,
            content_type="application/json"
        )

