from rest_framework import status
from rest_framework.response import Response
from .serializer import TaskSerializer,TaskDeleteSerializer
from .models import TaskModel
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(['POST'])
def task(request):
    # token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]  # Extract token from request headers
    serializer = TaskSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        task_name = serializer.validated_data['taskName']
        try:
            # if task already exists for the user update the task
            user = request.user.id
            existing_task = TaskModel.objects.get(taskName=task_name, user=user)
            serializer.update(existing_task, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TaskModel.DoesNotExist:
            # if task does not exist for the user create the task
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTasks(request):
    # get all tasks of user in ascending order
    tasks = TaskModel.objects.filter(user=request.user.id).order_by('average')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteTask(request):
    serializer = TaskDeleteSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        task_name = serializer.validated_data['taskName']
        try:
            # if exists -- >delete
            existing_task = TaskModel.objects.get(taskName=task_name, user=request.user.id)
            existing_task.delete()
            return Response({'message': 'Delete successful'},status=status.HTTP_200_OK)
        except TaskModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# authentication apis
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        user = User.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=user)
        return Response({'message': 'User Registration successful'},status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    Token.objects.filter(user=request.user).delete()
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)