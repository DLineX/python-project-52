from django.urls import path

from task_manager.users.views import (  # noqa: E501
    CreateUserView,
    DeleteUserView,
    ListUsersView,
    UpdateUserView,
)

urlpatterns = [
    path('', ListUsersView.as_view(), name='users_list'),
    path('create/', CreateUserView.as_view(), name='sign_in'),
    path('<int:pk>/update/', UpdateUserView.as_view(), name='update_user'),
    path('<int:pk>/delete/', DeleteUserView.as_view(), name='delete_user'),
]
