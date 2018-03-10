# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from course_app.models.students import StudentCourseMap
from models.courses import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'summary', 'is_deleted')
    list_filter = ('is_deleted', 'created_on')
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    # fields to show detailed layout
    # exclude to exclude from admin site
# admin.site.register(Course)


@admin.register(StudentCourseMap)
class StudentCourseMapAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'course_id', 'user_name', 'course_name')
    list_filter = ('user_id', 'course_id', 'is_deleted', 'created_on')
