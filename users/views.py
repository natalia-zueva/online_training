from rest_framework import serializers
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from materials.services import create_stripe_price, create_stripe_session
from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('course', 'lesson', 'payment_method',)
    ordering_fields = ('payment_date',)


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        course = serializer.validated_data.get('course')
        if not course:
            raise serializers.ValidationError('Укажите курс')

        payment = serializer.save()
        stripe_price_id = create_stripe_price(payment)
        payment.payment_link, payment.payment_id = create_stripe_session(stripe_price_id)
        payment.save()


