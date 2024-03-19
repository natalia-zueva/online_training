from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Subscription


@shared_task
def send_mail_update_course(course_pk):
    subscriptions= Subscription.objects.filter(course_id=course_pk)
    for sub in subscriptions:
        if sub.status:
            send_mail(
                subject="Обновление курса",
                message=f'Курс {sub.course.title} обновлен',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[sub.user.email],
                fail_silently=False
            )
