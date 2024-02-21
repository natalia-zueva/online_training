from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from materials.models import Lesson
from materials.serializers.lesson import LessonSerializer


class LessonDetailAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteAPIView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
