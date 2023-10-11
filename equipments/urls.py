from django.urls import path
from .views import input_equipment_view, home_view, home_view_after_input

app_name = 'equipments'

urlpatterns = [
    path('input', input_equipment_view, name="input"),
    path('home', home_view, name="home"),
    path('home_after_input', home_view_after_input, name="home_after_input"),
    path('', home_view, name="home"),
]