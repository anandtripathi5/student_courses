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
        requested_data = request.data
        set_password_functionality(request.user, **requested_data)
        return Response(
            data=True,
            status=200,
            content_type="application/json"
        )

