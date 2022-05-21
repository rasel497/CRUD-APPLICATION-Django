 
from django.urls import path
from .views import create, read, update, delete


urlpatterns = [
    path('new/', create, name='create'),
    path('', read, name='read'),
    path('<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]