import json

from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from course_app.functionality.student import register_student
from course_app.utils.resource_exception import handle_exceptions
from course_app.views.authentication import CsrfExemptSessionAuthentication


class StudentSignup(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    @handle_exceptions
    def post(self, request):
        request_data = request.data
        jwt_token = register_student(**request_data)
        return Response(
            data=jwt_token,
            status=status.HTTP_201_CREATED,
            content_type="application/json"
        )
