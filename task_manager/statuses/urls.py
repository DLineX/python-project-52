from django.urls import path

from task_manager.statuses.views import (  # noqa: E501
    CreateStatusView,
    DeleteStatusView,
    ListStatusView,
    UpdateStatusView,
)

urlpatterns = [
    path('', ListStatusView.as_view(), name='statuses_list'),
    path('create/', CreateStatusView.as_view(), name='create_status'),
    path('<int:pk>/update/', UpdateStatusView.as_view(), name='update_status'),
    path('<int:pk>/delete/', DeleteStatusView.as_view(), name='delete_status'),
]
