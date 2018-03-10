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
        """
            @api {post} /course/enroll Enroll student to a particular course
            @apiName Enroll Courses
            @apiGroup Student Courses
            @apiVersion 0.0.1

            @apiHeader {String} content_type application/json
            @apiHeader {String} Authorization jwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

            @apiParam {String} course_id id of the course to enroll student

            @apiSuccess {String} enrolled enrolled in case of success

            @apiParamExample e.g. Request Example
            {
                "course_id": "29424935-92bb-4ab9-a2c9-0ffe728b4a7c"
            }
            @apiSuccessExample e.g. Success-Response
            HTTP/1.1 201 OK
            "enrolled"

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
            @apiErrorExample Course Id not passed
            HTTP/1.1 400 KeyError
            {
            "message": "COURSE-ID-NOT-PASSED"
            }
            @apiErrorExample Duplicate course enroll not passed
            HTTP/1.1 400 KeyError
            {
            "message": "Duplicate entry '2942493592bb4ab9a2c90ffe728b4a7c-18' for key 'student_course_map_course_id_user_id_bbd3083b_uniq'"
            }

        """
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
        """
            @api {post} /course/leave Leave from a particular course
            @apiName Leave Courses
            @apiGroup Student Courses
            @apiVersion 0.0.1

            @apiHeader {String} content_type application/json
            @apiHeader {String} Authorization jwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

            @apiParam {String} course_id id of the course to leave student

            @apiSuccess {String} leave leave in case of success
            @apiParamExample e.g. Request Example
            {
                "course_id": "29424935-92bb-4ab9-a2c9-0ffe728b4a7c"
            }
            @apiSuccessExample e.g. Success-Response
            HTTP/1.1 201 OK
            "leave"

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
            @apiErrorExample Course Id not passed
            HTTP/1.1 400 KeyError
            {
            "message": "COURSE-ID-NOT-PASSED"
            }
            @apiErrorExample Not enrolled for a particular course
            HTTP/1.1 400 ValueError
            {
            "message": "USER-NOT-ENROLLED-FOR-GIVEN-COURSE"
            }

        """
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
        """
            @api {get} /course/available List of available course
            @apiName Available Courses
            @apiGroup Courses
            @apiVersion 0.0.1

            @apiHeader {String} content_type application/json

            @apiParam {String} course_id id of the course to leave student

            @apiSuccess {Object[]} List of dictionaries
            @apiSuccess {String} Object.course_id Id of the course available
            @apiSuccess {String} Object.course_name name of the available course
            @apiSuccess {String} Object.seats_left seats left for the available course

            @apiSuccessExample e.g. Success-Response
            HTTP/1.1 201 OK
            [
                {
                    "course_id": "29424935-92bb-4ab9-a2c9-0ffe728b4a7c",
                    "seats_left": 5,
                    "course_name": "Django ORM course"
                },
                {
                    "course_id": "2f64a063-3214-4fab-b4d7-885e0ea5a9fb",
                    "seats_left": 3,
                    "course_name": "management_course"
                }
            ]
        """
        response = get_available_course_list()
        return Response(
            data=response,
            status=200,
            content_type="application/json"
        )