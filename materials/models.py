from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course_preview', **NULLABLE, verbose_name='Превью')
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название урока')
    preview = models.ImageField(upload_to='lesson_preview', **NULLABLE, verbose_name='Превью')
    description = models.TextField(verbose_name='Описание урока', **NULLABLE)
    video_link = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)

    course = models.ForeignKey('materials.Course', on_delete=models.CASCADE, verbose_name='Урок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
