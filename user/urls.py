from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/', users, name='table_users'),
    path('detil/<int:id>', user_detil, name='user_detil'),
    path('edit<int:id>', user_edit, name='user_edit'),
    path('delete<int:id>', user_delete, name='user_delete'),
]