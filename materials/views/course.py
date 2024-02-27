from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.permissions import IsModerator, IsOwner
from materials.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated, IsModerator|IsOwner]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsModerator|IsOwner]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, IsModerator|IsOwner]
        elif self.action == 'delete':
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]
