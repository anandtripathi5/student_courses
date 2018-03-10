# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
from course_app.functionality.course_enrolled import student_course_enrolled
from course_app.models.courses import Course
from course_app.models.students import StudentCourseMap


class CourseEnrollTestCase(TestCase):
    def setUp(self):
        pass

    def test_course_not_found_course_enroll(self):
        user_obj = User.objects.create_user(username="anand", password="anand",
                                 email="anand")
        course_obj = Course.objects.create(course_name="flask")
        data = dict(
            course_id="30488c16-6682-44c9-8346-1c4b2ea8d378"
        )
        self.assertRaises(
            course_obj.DoesNotExist,
            student_course_enrolled,
            user_obj,
            **data
        )

    def test_course_deleted_course_enroll(self):
        user_obj = User.objects.create_user(username="anand",
                                            password="anand",
                                            email="anand")
        course_obj = Course.objects.create(course_name="flask", is_deleted=True)
        data = dict(
            course_id=str(course_obj.id)
        )
        self.assertRaises(
            course_obj.DoesNotExist,
            student_course_enrolled,
            user_obj,
            **data
        )

    def test_unavailable_course_enroll(self):
        course_obj = Course.objects.create(course_name="flask")
        user_list = ("anand", "anand1", "anand2", "anand3", "anand5")
        for user in user_list:
            user_obj = User.objects.create_user(
                username=user,
                password="anand",
                email="anand"
            )
            StudentCourseMap.objects.create(
                user_id=int(user_obj.id),
                course_id=str(course_obj.id),
                course_name=course_obj.course_name,
                user_name=user_obj.username
            )
        user_obj = User.objects.create_user(
            username="anand6",
            password="anand",
            email="anand"
        )
        data = dict(
            course_id=str(course_obj.id)
        )
        self.assertRaises(
            ValueError,
            student_course_enrolled,
            user_obj,
            **data
        )

    def test_available_course_enroll(self):
        course_obj = Course.objects.create(course_name="flask")
        user_obj = User.objects.create_user(
            username="anand",
            password="anand",
            email="anand"
        )
        data = dict(
            course_id=str(course_obj.id)
        )
        response = student_course_enrolled(user_obj, **data)
        self.assertEqual(response, "enrolled")