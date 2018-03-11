Student Courses
===================
Repo is having APIs related to students enrollment program.
**Base URL**
>- http://18.218.174.244:5000

**List of APIs**
>- Register Api
>- Login Api
>- Reset Password
>- Available Courses
>- Student Enrolled Courses
>- Enroll Course
>- Leave Course

----------
# **Admin Portal**
 1. Endpoint: http://18.218.174.244:5000/admin/

# **APIs description**
**Register Api**
 1. Endpoint URL: http://18.218.174.244:5000/register
 2. APIDoc: http://18.218.174.244:8080/doc/#api-Authentication-Signup

**Login Api**
 1. Endpoint URL: http://18.218.174.244:5000/login
 2. APIDoc: http://18.218.174.244:8080/doc/#api-Authentication-Login

**Reset Password**
 1. Endpoint URL: http://18.218.174.244:5000/student/password
 2. APIDoc: http://18.218.174.244:8080/doc/#api-Reset_Password-Reset_Password
 3. Jwt token provided from login api should be passed to this api in order to access this api

**Available Course**
 1. Endpoint URL: http://18.218.174.244:5000/course/available
 2. APIDoc: http://18.218.174.244:8080/doc/#api-Courses-Available_Courses

**Enroll Course**
 1. Endpoint URL: http://18.218.174.244:5000/course/enroll
 2. APIDoc: http://18.218.174.244:8080/doc/#api-Student_Courses-Enroll_Courses
 3. Course id from available course should be passed with Jwt token to this api in order to enroll a particular course

**Leave Course**
 1. Endpoint URL: http://18.218.174.244:5000/course/leave
 2. APIDoc: http://18.218.174.244:8080/doc/#api-Student_Courses-Leave_Courses
 3. Course id from available course should be passed with Jwt token to this api in order to leave a particular course

**Student Enrolled Courses**
 1. Endpoint URL: http://18.218.174.244:5000/course/student
 2. APIDoc: http://18.218.174.244:8080/doc/#api-Student_Courses-Student_Courses
 3. Jwt token should be passed to this api in order to get all the enrolled courses of a particular student



