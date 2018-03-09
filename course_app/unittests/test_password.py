# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase

# Create your unittests here.
from course_app.functionality.student_profile import set_password_functionality


class PasswordTestCase(TestCase):
    def setUp(self):
        pass

    def test_password_authentication_wrong_password(self):
        user_obj = User.objects.create_user(username="anand", password="anand",
                                            email="anand")
        self.assertRaises(
            ValueError,
            set_password_functionality,
            user_obj,
            current_password="tripathi",
            new_password="tripathi"
        )

    def test_password_authentication_password_not_provided(self):
        user_obj = User.objects.create_user(username="anand", password="anand",
                                            email="anand")
        self.assertRaises(
            KeyError,
            set_password_functionality,
            dict()
        )

    def test_password_functionality(self):
        user_obj = User.objects.create_user(username="anand", password="anand",
                                            email="anand")
        set_password_functionality(
            user_obj,
            current_password="anand",
            new_password="tripathi"
        )
        user_obj = authenticate(username="anand", password="tripathi")
        self.assertEqual(user_obj.username,"anand")


