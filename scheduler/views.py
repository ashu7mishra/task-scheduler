from django.shortcuts import render
from rest_framework import generics, status
from .models import Task, TaskDependency
from .serializer import TaskSerializer, TaskDependencySerializer


# task views
class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    
# task dependency views

class TaskDependencyListCreateAPIView(generics.ListCreateAPIView):
    queryset = TaskDependency.objects.all()
    serializer_class = TaskDependency
    
class TaskDependencyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskDependency.objects.all()
    serializer_class = TaskDependency
