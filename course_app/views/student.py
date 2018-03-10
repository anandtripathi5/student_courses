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
        """
            @api {get} /course/student Student Enrolled Courses
            @apiName Student Courses
            @apiGroup Student Courses
            @apiVersion 0.0.1

            @apiHeader {String} content_type application/json
            @apiHeader {String} Authorization jwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

            @apiSuccess {Object[]} List of dictionaries
            @apiSuccess {String} Object.course_id Id of the course the student is enrolled in
            @apiSuccess {String} Object.course_name name of the course the student is enrolled in

            @apiSuccessExample e.g. Success-Response
            HTTP/1.1 201 OK
            [
                {
                    "course_id": "2f64a063-3214-4fab-b4d7-885e0ea5a9fb",
                    "course_name": "management_course"
                }
            ]
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
            @apiErrorExample User Not found
            HTTP/1.1 400 ValueError
            {
            "message": "USER-NOT-FOUND"
            }
        """
        response = get_student_course_list(request.user)
        return Response(
            data=response,
            status=200,
            content_type="application/json"
        )