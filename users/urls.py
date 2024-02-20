from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentListAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payments_list'),
]