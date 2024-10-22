from django.urls import path
from . import views

urlpatterns = [
    path('testing2/',views.testing2,name='testing2'),
    path('testing/', views.testing, name='testing'), 
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]