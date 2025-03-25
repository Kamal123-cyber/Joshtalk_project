from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Task
from useraccount.models import UserAccount
from .serializers import TaskSerializer, AssignTaskSerializer

#This is for Creating a Task, you can pass the user with it to the task
class CreateTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#This is for Assigning a Task to one user or multiple users
class AssignTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AssignTaskSerializer(data=request.data)
        if serializer.is_valid():
            users = serializer.validated_data['user_ids']
            task.assigned_users.set(users)
            return Response({"message": "Users assigned successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#This is for Getting all Task that is assigned to a particular user by the user id
class UserTasksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = UserAccount.objects.get(id=user_id)
        except UserAccount.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
