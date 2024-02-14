from django.urls import path
from rest_framework import routers

from materials.apps import MaterialsConfig
from materials.views.course import CourseViewSet
from materials.views.lesson import *

app_name = MaterialsConfig.name


urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('<int:pk>', LessonDetailView.as_view(), name='lesson_detail'),
    path('<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('create/', LessonCreateView.as_view(), name='lesson_create'),
    path('<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls