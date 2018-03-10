from function_logger import function_logger
from function_validator import req_validator
from course_app.constants.common_constants import DEFAULT_MAX_COURSE_SEAT
from course_app.models.courses import Course
from course_app.models.students import StudentCourseMap
from course_app.utils.logger import logger


@function_logger(logger)
@req_validator(param_name="course_id",
               err_description="COURSE-ID-NOT-PASSED",
               req=True, var_type=basestring)
def student_course_enrolled(user_obj, **kwargs):
    course_id = kwargs.get("course_id")
    course_obj = Course.objects.get(id=course_id, is_deleted=False)
    enrolled_obj = StudentCourseMap.objects.filter(course_id=course_id,
                                                   is_deleted=False).all()
    if len(enrolled_obj) >= DEFAULT_MAX_COURSE_SEAT:
        raise ValueError("COURSE-FULL")
    # already enrolled student will be handled through unique key
    course_enrolled = StudentCourseMap.objects.create(
        user_id=int(user_obj.id),
        user_name=user_obj.username,
        course_id=str(course_id),
        course_name=course_obj.course_name
    )
    course_enrolled.save()
    return "enrolled"