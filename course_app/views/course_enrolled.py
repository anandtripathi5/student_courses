from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from course_app.functionality.course_enrolled import student_course_enrolled
from course_app.functionality.course_leave import student_course_leave
from course_app.functionality.courses import get_available_course_list
from course_app.utils.resource_exception import handle_exceptions
from course_app.views.authentication import CustomAuthentication, \
    CsrfExemptSessionAuthentication


class CourseEnrolled(APIView):
    authentication_classes = (
        CustomAuthentication,
        CsrfExemptSessionAuthentication,
        BasicAuthentication
    )

    @handle_exceptions
    def post(self, request):
        requested_data = request.data
        response = student_course_enrolled(request.user, **requested_data)
        return Response(
            data=response,
            status=200,
            content_type="application/json"
        )


class CourseLeave(APIView):
    authentication_classes = (
        CustomAuthentication,
        CsrfExemptSessionAuthentication,
        BasicAuthentication
    )

    @handle_exceptions
    def post(self, request):
        requested_data = request.data
        response = student_course_leave(request.user, **requested_data)
        return Response(
            data=response,
            status=200,
            content_type="application/json"
        )


class AvailableCourseList(APIView):
    authentication_classes = (
        CsrfExemptSessionAuthentication,
        BasicAuthentication
    )

    @handle_exceptions
    def get(self, request):
        response = get_available_course_list()
        return Response(
            data=response,
            status=200,
            content_type="application/json"
        )