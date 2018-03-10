from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from course_app.functionality.student import login_functionality
from course_app.utils.resource_exception import handle_exceptions
from course_app.views.authentication import CsrfExemptSessionAuthentication


class Login(APIView):
    """
        @api {post} /login Login method
        @apiName Login
        @apiGroup Authentication
        @apiVersion 0.0.1

        @apiHeader {String} content_type application/json

        @apiParam {String} user_name user_name of the student for login purpose
        @apiParam {String} password password of the student for login purpose

        @apiSuccess {String} token jwt token return having lifetime of 1 hour, use
        this token to access other apis

        @apiParamExample e.g. Request Example
        {
            "user_name": "anand",
            "password": "anand"
        }


        @apiSuccessExample e.g. Success-Response
        HTTP/1.1 200 OK
           {
              "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX"
           }
        @apiErrorExample User name not provided
        HTTP/1.1 400 KeyError
        {
        "message": "USER-NAME-NOT-PASSED"
        }
        @apiErrorExample password not provided
        HTTP/1.1 400 KeyError
        {
        "message": "PASSWORD-NOT-PASSED"
        }
        @apiErrorExample User not found
        HTTP/1.1 400 ValueError
        {
        "message": "USER-NOT-FOUND"
        }
        @apiErrorExample Credentials not matched
        HTTP/1.1 400 ValueError
        {
        "message": "INVALID-CREDENTIALS"
        }

    """
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    @handle_exceptions
    def post(self, request):
        request_data = request.data
        jwt_token = login_functionality(request, **request_data)
        return Response(
            data=jwt_token,
            status=200,
            content_type="application/json"
        )

