from django.urls import path
from .api_views import CreateTaskView, AssignTaskView, UserTasksView

urlpatterns = [
    path("create/", CreateTaskView.as_view(), name="create-task"),
    path("tasks/<uuid:task_id>/assign/", AssignTaskView.as_view(), name="assign-task"),
    path("tasks/user/<uuid:user_id>/", UserTasksView.as_view(), name="user-tasks"),
]
