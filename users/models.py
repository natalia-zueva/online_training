from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None

    email = models.EmailField(unique='True', verbose_name='Email')

    first_name = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name='фамилия', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    roles = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)

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
    payment_link = models.URLField(max_length=400, verbose_name='ссылка для оплаты', **NULLABLE)
    payment_id = models.CharField(max_length=255, verbose_name='идентификатор платежа', **NULLABLE)

    def __str__(self):
        return f"{self.user}: ({self.course})"

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежы"