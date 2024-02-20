from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson
from materials.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lesson_in_course = LessonSerializer(source='lesson_set', many=True)

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()


    class Meta:
        model = Course
        fields = '__all__'


