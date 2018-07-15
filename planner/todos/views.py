from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer


class TodoListView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(assignee=self.request.user)

    def perform_create(self, serializer):
        serializer.save(assignee=self.request.user)


class TodoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(assignee=self.request.user)
