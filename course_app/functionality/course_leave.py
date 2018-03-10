from function_logger import function_logger
from function_validator import req_validator
from course_app.models.students import StudentCourseMap
from course_app.utils.logger import logger


@function_logger(logger)
@req_validator(param_name="course_id",
               err_description="COURSE-ID-NOT-PASSED-COURSE-LEAVE",
               req=True, var_type=basestring)
def student_course_leave(user_obj, **kwargs):
    course_id = kwargs.get("course_id")
    obj = StudentCourseMap.objects.filter(
        course_id=course_id,
        user_id=int(user_obj.id)
    )
    if not obj:
        raise ValueError("USER-NOT-ENROLLED-FOR-GIVEN-COURSE")
    obj.delete()
    return "leave"
