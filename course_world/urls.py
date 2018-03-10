"""course_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from course_app.views.course_enrolled import CourseEnrolled, CourseLeave, \
    AvailableCourseList
from course_app.views.login import Login
from course_app.views.password import PasswordReset
from course_app.views.register import StudentSignup
from course_app.views.student import StudentAvailableCourseList
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register', StudentSignup.as_view(), name="student-register"),
    url(r'^login', Login.as_view(), name="student-login"),
    url(r'^student/password', PasswordReset.as_view(), name="password-reset"),
    url(r'^course/enroll', CourseEnrolled.as_view(), name="student-course-enroll"),
    url(r'^course/leave', CourseLeave.as_view(), name="student-course-leave"),
    url(r'^course/student', StudentAvailableCourseList.as_view(), name="student-course-leave"),
    url(r'^course/available', AvailableCourseList.as_view(), name="student-course-leave")
]
