import json
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.generic.base import View
from marshmallow import fields
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from webargs.djangoparser import use_args

from course_app.functionality.student_profile import set_password_functionality
from course_app.utils.resource_exception import handle_exceptions
from course_app.views.authentication import CustomAuthentication, \
    CsrfExemptSessionAuthentication


class PasswordReset(APIView):
    authentication_classes = (CustomAuthentication, CsrfExemptSessionAuthentication, BasicAuthentication)

    @handle_exceptions
    def post(self, request):
        requested_data = request.data
        set_password_functionality(request.user, **requested_data)
        return Response(
            data=True,
            status=200,
            content_type="application/json"
        )

