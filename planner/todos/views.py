from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TodoSerializer


class TodoListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(assignee=self.request.user)

    def perform_create(self, serializer):
        serializer.save(assignee=self.request.user)


class TodoView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(assignee=self.request.user)
