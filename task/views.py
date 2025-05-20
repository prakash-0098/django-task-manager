from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import task


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
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
def createTask(request):
    if request.method == 'GET':
        tasks = task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(
            serializer.data, 
            status = status.HTTP_200_OK)

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


@api_view(['GET', 'PUT', 'DELETE'])
def taskDetails(request, pk):
    try:
        tasks = task.objects.get(pk=pk, user=request.user)
    except task.DoesNotExist:
        return Response({
            'error': 'Task not found'
        }, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TaskSerializer(tasks)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(tasks, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )
        
    elif request.method == 'DELETE':
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
