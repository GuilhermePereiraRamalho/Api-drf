from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CourseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Student')
router.register('courses', CourseViewSet, basename='Course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
