from django.contrib.auth import authenticate
from function_logger import function_logger
from function_validator import req_validator

from course_app.utils.logger import logger


@function_logger(logger)
@req_validator(param_name="current_password",
               err_description="CURRENT-PASSWORD-NOT-PASSED",
               req=True, var_type=basestring)
@req_validator(param_name="new_password", err_description="NEW-PASSWORD-NOT-PASSED",
               req=True, var_type=basestring)
def set_password_functionality(user_obj, **kwargs):
    is_auth = authenticate(
        username=user_obj.username,
        password=kwargs.get("current_password")
    )
    if not is_auth:
        raise ValueError("CURRENT-PASSWORD-DOESNT-MATCH")
    user_obj.set_password(kwargs.get("new_password"))
    user_obj.save()
