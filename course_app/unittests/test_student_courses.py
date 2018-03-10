# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase

from course_app.functionality.course_enrolled import student_course_enrolled
from course_app.functionality.course_leave import student_course_leave
from course_app.functionality.courses import get_available_course_list, \
    get_student_course_list
from course_app.models.courses import Course
from course_app.models.students import StudentCourseMap


class StudentAvailableCourseListTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_not_found_student_course_list(self):
        self.assertRaises(
            TypeError,
            get_student_course_list
        )

    def test_deleted_course_found_student_course_list(self):
        course_obj = Course.objects.create(course_name="flask", is_deleted=True)
        user_obj = User.objects.create_user(
            username="anand",
            password="anand",
            email="anand"
        )
        StudentCourseMap.objects.create(
            user_id=int(user_obj.id),
            course_id=str(course_obj.id),
            user_name=user_obj.username,
            course_name=course_obj.course_name
        )
        response = get_student_course_list(user_obj)
        self.assertEqual(
            [],
            response
        )

    def test_leaved_user_available_course_list(self):
        course_obj = Course.objects.create(course_name="flask")
        user_obj = User.objects.create_user(
            username="anand",
            password="anand",
            email="anand"
        )
        student_course_enrolled(user_obj, course_id=str(course_obj.id))
        student_course_leave(user_obj, course_id=str(course_obj.id))
        response = get_student_course_list(user_obj)
        self.assertEqual(
            [],
            response
        )

    def test_user_available_course_list(self):
        course_obj = Course.objects.create(course_name="flask")
        user_obj = User.objects.create_user(
            username="anand",
            password="anand",
            email="anand"
        )
        student_course_enrolled(user_obj, course_id=str(course_obj.id))
        response = get_student_course_list(user_obj)
        self.assertEqual(
            [dict(
                course_id=str(course_obj.id),
                course_name=course_obj.course_name
            )],
            response
        )
