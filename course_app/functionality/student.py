import jwt
from function_logger import function_logger
from course_app.utils.logger import logger
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from course_world.settings import SECRET_KEY


@function_logger(logger)
def dump_student(**kwargs):
    student_obj = User.objects.create_user(
        username=kwargs.get("user_name"),
        email=kwargs.get("email"),
        password=kwargs.get("password")
    )
    student_obj.save()
    return int(student_obj.id)


@function_logger(logger)
def register_student(**kwargs):
    student_id = dump_student(**kwargs)
    jwt_token = dict(token=jwt.encode(dict(user_id=student_id), SECRET_KEY))
    return jwt_token


@function_logger(logger)
def login_authentication(**kwargs):
    user_name = kwargs.get('user_name')
    password = kwargs.get('password')
    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        raise ValueError("User Not found")
    authentication = authenticate(username=user_name, password=password)
    if not authentication:
        raise ValueError("Invalid credentials")
    return user, authentication


@function_logger(logger)
def login_functionality(request, **kwargs):
    user, authentication = login_authentication(**kwargs)
    if authentication.is_authenticated:
        login(request, authentication)
    jwt_token = {'token': jwt.encode(dict(user_id=user.id), SECRET_KEY)}
    return jwt_token

