from rest_framework import serializers
from .models import Task
from useraccount.models import UserAccount


# These are the serializers for Task operations
class TaskSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(
        queryset=UserAccount.objects.all(), many=True, required=False
    )

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'task_type', 'status', 'completed_at', 'assigned_users']

class AssignTaskSerializer(serializers.Serializer):
    user_ids = serializers.ListField(
        child=serializers.UUIDField(),
        write_only=True
    )

    def validate_user_ids(self, value):
        users = UserAccount.objects.filter(id__in=value)
        if len(users) != len(value):
            raise serializers.ValidationError("One or more users not found.")
        return users
