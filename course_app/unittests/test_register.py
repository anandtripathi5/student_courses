# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase

# Create your unittests here.
from course_app.functionality.student import dump_student


class LoginTestCase(TestCase):
    def setUp(self):
        pass

    def test_login_authentication_already_created(self):
        User.objects.create_user(username="anand", password="anand", email="anand")
        data = dict(
            user_name="anand",
            password="anand",
            email="anand"
        )
        self.assertRaises(
            IntegrityError,
            dump_student,
            **data
        )

    def test_login_authentication_username_not_provided(self):
        data = dict(password="anand")
        self.assertRaises(
            ValueError,
            dump_student,
            **data
        )

    def test_register_functionality(self):
        user_id = dump_student(**dict(user_name="anand", password="anand"))
        get_user_name = User.objects.get(username="anand")
        self.assertEqual(user_id, get_user_name.id)


