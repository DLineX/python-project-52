from django.urls import path

from task_manager.labels.views import (  # noqa: E501
    CreateLabelsView,
    DeleteLabelsView,
    ListLabelsView,
    UpdateLabelsView,
)

urlpatterns = [
    path('', ListLabelsView.as_view(), name='labels_list'),
    path('create/', CreateLabelsView.as_view(), name='create_label'),
    path('<int:pk>/update/', UpdateLabelsView.as_view(), name='update_label'),
    path('<int:pk>/delete/', DeleteLabelsView.as_view(), name='delete_label'),
]
