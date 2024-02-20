from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView

from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('course', 'lesson', 'payment_method',)
    ordering_fields = ('payment_date',)


