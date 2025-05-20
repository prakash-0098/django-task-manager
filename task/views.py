from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Task

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data = request.data)
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

@api_view(['POST', 'GET'])
@permission_classes([permissions.IsAuthenticated])
def createTaskAndList(request):
    if request.method == 'GET':
        task = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(task, many=True)
        return Response(
            serializer.data,
            status = status.HTTP_200_OK
        )

    elif request.method == 'POST':
        serializer = TaskSerializer(data = request.data)
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
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def modifyTask(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)
    except Task.DoesNotExist:
        return Response({
            'error': 'Task not found'
        }, status = status.HTTP_404_NOT_FOUND)
    
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
