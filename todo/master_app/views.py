from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import TodoSerializer

from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()