# apis/views.py
from rest_framework import viewsets

from todos.models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
      print(self.queryset.filter(title='666').query)
      return self.queryset