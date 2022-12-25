from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('artikel/', artikel, name='table_artikel'),
    path('artikel/tambah/', artikel_tambah, name='artikel_tambah'),
    path('artikel/view/<str:id>', view_artikel, name='view_artikel'),
    path('artikel/edit/<str:id>', edit_artikel, name='edit_artikel'),
    path('artikel/delete/<str:id>', delete_artikel, name='delete_artikel'),
    
    # api
    path('api/artikel/list/<str:x_api_key>', artikel_list, name='artikel_list')
]