from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Subscription


class SubscribeAPIView(APIView):

    def post(self, *args, **kwargs):

        user = self.request.user
        course_id = self.request.data.get('course_id')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.status = False
            message = 'Вы отписались от обновлений курса'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Вы подписаны на обновления курса'

        return Response({"message": message})


