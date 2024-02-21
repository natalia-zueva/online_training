from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique='True', verbose_name='Email')

    first_name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name='фамилия', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, verbose_name='пользователь')
    payment_date = models.DateField(verbose_name='дата оплаты', **NULLABLE)
    course = models.ForeignKey('materials.Course',
                               on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey('materials.Lesson',
                               on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    payment_method = models.CharField(max_length=50,
                                      choices=(('CARD', 'картой'), ('CASH', 'наличными')),
                                      verbose_name='способ оплаты', **NULLABLE)
