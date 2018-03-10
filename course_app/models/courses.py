# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from datetime import datetime
from django.db import models

# Create your models here.

from django.urls import \
    reverse  # Used to generate URLs by reversing the URL patterns


class Course(models.Model):
    """
    Model representing a Courses for students (but not a specific copy of a
    course).
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for the course"
    )
    course_name = models.CharField(
        max_length=200, unique=True,
        help_text="Name of the course"
    )
    summary = models.TextField(
        max_length=1000,
        help_text='Enter a brief description of the course',
        blank=True
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text='Course availability'
    )
    duration_in_days = models.IntegerField(
        default=1,
        help_text='Duration of course in days',
        blank=True
    )
    price = models.IntegerField(
        default=100,
        help_text='Price in dollar of course',
        blank=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text='created date of course'
    )
    modified_on = models.DateTimeField(
        auto_now=True,
        help_text='modified date of course'
    )

    class Meta:
        db_table = "course"

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.course_name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('course-details', args=[str(self.id)])
