from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.add, name='add'),
    path('delete/<int:id>/', views.deleteForm , name='deleteForm'),
    path('edit/<int:id>/', views.edit , name='edit'),
]