from django.shortcuts import render
from rest_framework import generics, status, views, response
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
    
    
# Graph + scheduling view
class TaskExecutionOrderView(views.APIView):
    def get(self, request):
        graph, all_nodes = GraphBuilder().build_graph()
        scheduler = SchedulerService(graph, all_nodes)
        
        if scheduler.has_cycle():
            return response.Response(
                {'error': 'Cycle Detected. Cannot generate execution order.'}
                status=status.HTTP_400_BAD_REQUEST
            )
            
        order = scheduler.topological_sort()
        ordered_task = Task.objects.filter(id__in=order)
        serialized = TaskSerializer(ordered_task, many=True)
        return response.Response(serialized.data)
    
    
class TaskDetectionView(views.APIView):
    def get(self, request):
        graph, all_nodes = GraphBuilder().build_graph()
        scheduler = SchedulerService(graph, all_nodes)
        return response.Response({"has cycle:", scheduler.has_cycle()})
        
    
