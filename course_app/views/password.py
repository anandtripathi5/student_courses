from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from course_app.functionality.student_profile import set_password_functionality
from course_app.utils.resource_exception import handle_exceptions
from course_app.views.authentication import CustomAuthentication, \
    CsrfExemptSessionAuthentication


class PasswordReset(APIView):
    authentication_classes = (CustomAuthentication, CsrfExemptSessionAuthentication, BasicAuthentication)

    @handle_exceptions
    def post(self, request):
        """
            @api {post} /student/password Reset Password
            @apiName Reset Password
            @apiGroup Reset Password
            @apiVersion 0.0.1

            @apiHeader {String} content_type application/json
            @apiHeader {String} Authorization jwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

            @apiParam {String} current_password current password of user for reset password
            @apiParam {String} new_password new password of the student for reset password

            @apiSuccess {String} true true for success response

            @apiParamExample e.g. Request Example
            {
                "current_password": "anand",
                "new_password": "anand"
            }

            @apiSuccessExample e.g. Success-Response
            HTTP/1.1 201 OK
            true

            @apiErrorExample Jwt expired
            HTTP/1.1 403 Forbidden
            {
            "detail": "Signature has expired"
            }
            @apiErrorExample Invalid JWT header
            HTTP/1.1 403 Forbidden
            {
            "detail": "JWT Invalid Header"
            }
            @apiErrorExample JWT decode error
            HTTP/1.1 403 Forbidden
            {
            "detail": "Invalid header string: 'utf8' codec can't decode byte
            0xc6 in position 2: invalid continuation byte"
            }
            @apiErrorExample current password not provided
            HTTP/1.1 400 KeyError
            {
            "message": "CURRENT-PASSWORD-NOT-PASSED"
            }
            @apiErrorExample new password not provided
            HTTP/1.1 400 KeyError
            {
            "message": "NEW-PASSWORD-NOT-PASSED"
            }
            @apiErrorExample Password doesn't match with existing password
            HTTP/1.1 400 ValueError
            {
            "message": "CURRENT-PASSWORD-DOESNT-MATCH"
            }
        """
        requested_data = request.data
        set_password_functionality(request.user, **requested_data)
        return Response(
            data=True,
            status=200,
            content_type="application/json"
        )

