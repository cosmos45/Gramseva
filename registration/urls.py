from . import views
from django.urls import path

app_name = 'registration'

urlpatterns = [
    path('', views.Registration, name='registration'),
    path('Add_data/', views.Add_data, name='Add_data'),

    ]