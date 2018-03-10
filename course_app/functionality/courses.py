from function_logger import function_logger
from course_app.constants.common_constants import DEFAULT_MAX_COURSE_SEAT
from course_app.models.courses import Course
from course_app.models.students import StudentCourseMap
from course_app.utils.logger import logger


@function_logger(logger)
def get_available_course_list():
    course_list = []
    course_obj = Course.objects.filter(is_deleted=False).all()
    for course in course_obj:
        enrolled_obj = StudentCourseMap.objects.filter(
            course_id=str(course.id),
            is_deleted=False
        ).all()
        if len(enrolled_obj) < DEFAULT_MAX_COURSE_SEAT:
            course_list.append(dict(
                course_id=str(course.id),
                course_name=course.course_name,
                seats_left = DEFAULT_MAX_COURSE_SEAT - len(enrolled_obj)
            ))
    return course_list


@function_logger(logger)
def get_student_course_list(user_obj):
    if not user_obj:
        raise ValueError("USER-NOT-FOUND")
    course_list = []
    course_obj = StudentCourseMap.objects.filter(
        user=int(user_obj.id),
        is_deleted=False,
        course__is_deleted=False
    ).select_related(
        'course'
    ).all()
    for course in course_obj:
        course_list.append(
            dict(
                course_id=str(course.course_id),
                course_name=course.course_name
            )
        )
    return course_list
