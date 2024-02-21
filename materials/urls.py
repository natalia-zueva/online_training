from django.urls import path
from rest_framework import routers

from materials.apps import MaterialsConfig
from materials.views.course import CourseViewSet
from materials.views.lesson import LessonListAPIView, LessonDetailAPIView, LessonUpdateAPIView, LessonCreateAPIView, \
    LessonDeleteAPIView

app_name = MaterialsConfig.name

urlpatterns = [
    path('', LessonListAPIView.as_view(), name='lesson_list'),
    path('<int:pk>', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('<int:pk>/delete/', LessonDeleteAPIView.as_view(), name='lesson_delete'),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls
