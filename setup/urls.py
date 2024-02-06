from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CourseViewSet, RegistrationViewSet, ListStudentRegistration, ListStudentOnCourse
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Student')
router.register('courses', CourseViewSet, basename='Course')
router.register('registrations', RegistrationViewSet, basename='Registration')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/registrations/', ListStudentRegistration.as_view()),
    path('course/<int:pk>/registrations/', ListStudentOnCourse.as_view()),
]
