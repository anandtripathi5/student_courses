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
        """
            @api {post} /register Signup method
            @apiName Signup
            @apiGroup Authentication
            @apiVersion 0.0.1

            @apiHeader {String} content_type application/json

            @apiParam {String} user_name user_name of the student for signup purpose
            @apiParam {String} password password of the student for signup purpose
            @apiParam {String} email email of the student for signup purpose

            @apiSuccess {String} token jwt token return having lifetime of 1 hour, use
            this token to access other apis

            @apiParamExample e.g. Request Example
            {
                "user_name": "anand",
                "password": "anand",
                "email": "anand@anand.com"
            }

            @apiSuccessExample e.g. Success-Response
            HTTP/1.1 201 OK
               {
                  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX"
               }
            @apiErrorExample User name not provided
            HTTP/1.1 400 KeyError
            {
            "message": "USER-NAME-NOT-PASSED-REGISTER-CALL"
            }
            @apiErrorExample password not provided
            HTTP/1.1 400 KeyError
            {
            "message": "PASSWORD-NOT-PASSED-REGISTER-CALL"
            }
            @apiErrorExample Duplicate registration
            HTTP/1.1 400 ValueError
            {
            "message": "Duplicate entry 'anand4' for key 'username'"
            }
        """
        request_data = request.data
        jwt_token = register_student(**request_data)
        return Response(
            data=jwt_token,
            status=status.HTTP_201_CREATED,
            content_type="application/json"
        )
