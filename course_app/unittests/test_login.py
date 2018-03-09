# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase

# Create your unittests here.
from course_app.functionality.student import login_authentication


class LoginTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="anand", password="anand", email="anand")

    def test_login_authentication_invalid_credential(self):
        data = dict(user_name="anand", password="password")
        self.assertRaises(
            ValueError,
            login_authentication,
            **data
        )

    def test_login_authentication_user_not_found(self):
        data = dict(user_name="nand", password="password")
        self.assertRaises(
            ValueError,
            login_authentication,
            **data
        )

    def test_login_authentication(self):
        data = dict(user_name="anand", password="anand")
        user, authentication = login_authentication(**data)
        self.assertEqual(authentication.is_authenticated, True)


