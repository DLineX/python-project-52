from django.urls import path

from task_manager.tasks.views import (  # noqa: E501
    CreateTasksView,
    DeleteTasksView,
    DetailTasksView,
    ListTasksView,
    UpdateTasksView,
)

urlpatterns = [
    path('', ListTasksView.as_view(), name='tasks_list'),
    path('<int:pk>/', DetailTasksView.as_view(), name='show_tasks'),
    path('create/', CreateTasksView.as_view(), name='create_task'),
    path('<int:pk>/update/', UpdateTasksView.as_view(), name='update_task'),
    path('<int:pk>/delete/', DeleteTasksView.as_view(), name='delete_task'),
]
