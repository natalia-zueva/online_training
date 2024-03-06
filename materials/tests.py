from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user =User.objects.create(
            email="test@test.ru",
            is_staff = True,
            is_active = True,
            is_superuser = False,
        )
        self.user.set_password("test_user")
        self.user.save()

        self.course = Course.objects.create(
            title="Test_course",
            description="Test_course",
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            title='Test_lesson',
            description='Test_lesson',
            owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_list_lessons(self):
        """Тестирование вывода списка уроков"""

        response = self.client.get(
            reverse('materials:lesson_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                {
                    'id': self.lesson.id,
                    'title': self.lesson.title,
                    'preview': self.lesson.preview,
                    'description': self.lesson.description,
                    'video_link': self.lesson.video_link,
                    'course': self.lesson.course,
                    'owner': self.user.id
                }
                ]
            }
        )

    def test_create_lesson(self):
        """Тестирование создания урока"""

        data = {
            "title": "test_lesson2",
            "description": "test_lesson2",
            "course": 1
        }

        response = self.client.post(
            reverse('materials:lesson_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json()['title'],
            data['title']
        )

    def test_update_lesson(self):
        """Тестирование изменения информации об уроке"""
        lesson = Lesson.objects.create(
            title='Test_lesson',
            description='Test_lesson',
            owner=self.user
        )

        response = self.client.patch(
            f'/material/{lesson.id}/update/',
            {'description': 'change'}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        lesson = Lesson.objects.create(
            title='Test_lesson',
            description='Test_lesson',
            owner=self.user
        )

        response = self.client.delete(
            f'/material/{lesson.id}/delete/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.ru",
            is_staff=True,
            is_active=True,
            is_superuser=False,
        )
        self.user.set_password("test_user")
        self.user.save()

        self.course = Course.objects.create(
            title="Test_course",
            description="Test_course",
            owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        """Тест на создание подписки на курс"""

        data = {
            "user": self.user.id,
            "course": self.course.id,
        }

        response = self.client.post(
            reverse('materials:subscribe'),
            data=data
        )
        print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'message': 'Вы подписались на обновления курса'}
        )
