from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from course_app.functionality.courses import get_student_course_list
from course_app.utils.resource_exception import handle_exceptions
from course_app.views.authentication import CustomAuthentication, \
    CsrfExemptSessionAuthentication


class StudentAvailableCourseList(APIView):
    authentication_classes = (
        CustomAuthentication,
        CsrfExemptSessionAuthentication,
        BasicAuthentication
    )

    @handle_exceptions
    def get(self, request):
        response = get_student_course_list(request.user)
        return Response(
            data=response,
            status=200,
            content_type="application/json"
        )