# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase

from course_app.functionality.course_enrolled import student_course_enrolled
from course_app.functionality.course_leave import student_course_leave
from course_app.models.courses import Course
from course_app.models.students import StudentCourseMap


class CourseLeaveTestCase(TestCase):
    def setUp(self):
        pass

    def test_course_not_found_course_leave(self):
        user_obj = User.objects.create_user(username="anand",
                                            password="anand",
                                            email="anand")
        data = dict(
            course_id="30488c16-6682-44c9-8346-1c4b2ea8d378"
        )
        self.assertRaises(
            ValueError,
            student_course_leave,
            user_obj,
            **data
        )

    def test_course_id_not_provided_course_leave(self):
        user_obj = User.objects.create_user(username="anand",
                                            password="anand",
                                            email="anand")
        self.assertRaises(
            KeyError,
            student_course_leave,
            user_obj
        )

    def test_available_course_leave(self):
        course_obj = Course.objects.create(course_name="flask")
        user_obj = User.objects.create_user(
            username="anand",
            password="anand",
            email="anand"
        )
        data = dict(
            course_id=str(course_obj.id)
        )
        student_course_enrolled(user_obj, **data)
        response = student_course_leave(user_obj, **data)
        self.assertEqual(response, "leave")