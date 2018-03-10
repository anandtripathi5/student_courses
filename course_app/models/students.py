# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse

from course_app.models.courses import Course


class StudentCourseMap(models.Model):
    """
    Model representing a Courses for students (but not a specific copy of a
    course).
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="primary key of stundent enrolled"
    )
    user_id = models.ForeignKey(
        User,
        help_text="foreign key of student"
    )
    course_id = models.ForeignKey(
        Course,
        help_text='foreign key of course'
    )
    course_name = models.TextField(
        max_length=200,
        help_text="Name of the course student enrolled"
    )
    user_name = models.TextField(
        max_length=150,
        help_text="Name of the student enrolled for course"
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text='Course availability'
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text='created date of course'
    )
    modified_on = models.DateTimeField(
        auto_now=True,
        help_text='modified date of course'
    )
    models.Index(fields=['user_id', 'course_id'])

    class Meta:
        db_table = "student_course_map"

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user_id

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('students-enrolled', args=[str(self.id)])
