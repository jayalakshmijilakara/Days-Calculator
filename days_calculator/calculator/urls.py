from django.urls import path
from . import views

urlpatterns = [
    path('', views.days_calculator, name='days_calculator'),
]
