from rest_framework.decorators import api_view
from .serializers import UserSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Task

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status = status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
    )

@api_view(['GET', 'POST'])
def create_and_list_task(request):
    if request.method == 'GET':
        task = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(task, many=True)
        
        if len(serializer.data) < 1:
            return Response({
                'message': 'Not Found'
            }, status = status.HTTP_404_NOT_FOUND)
        
        return Response(
            serializer.data,
            status = status.HTTP_200_OK
        )

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

@api_view(['PUT', 'GET', 'DELETE'])
def modify_task(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)
    except Task.DoesNotExist:
        return Response({
            'error': 'Task not found'
        })
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(
            serializer.data,
            status = status.HTTP_200_OK
        )
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )
        
    elif request.method == 'DELETE':
        task.delete()
        return Response(
            status = status.HTTP_204_NO_CONTENT
        )