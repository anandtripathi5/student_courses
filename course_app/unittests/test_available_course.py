# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
from course_app.functionality.courses import get_available_course_list
from course_app.models.courses import Course
from course_app.models.students import StudentCourseMap


class AvailableCourseListTestCase(TestCase):
    def setUp(self):
        pass

    def test_empty_course_list(self):
        response = get_available_course_list()
        self.assertEqual(response, [])

    def test_deleted_course_list(self):
        Course.objects.create(course_name="flask", is_deleted=True)
        response = get_available_course_list()
        self.assertEqual(response, [])

    def test_unavailable_course_list(self):
        user_list = ("anand", "anand1", "anand2", "anand3", "anand5")
        course_obj = Course.objects.create(course_name="flask")
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
        response = get_available_course_list()
        self.assertEqual(response, [])

    def test_available_course_list(self):
        course_obj = Course.objects.create(course_name="flask")
        response = get_available_course_list()
        self.assertEqual(response, [dict(
            course_id=str(course_obj.id),
            course_name=course_obj.course_name,
            seats_left=5
        )])