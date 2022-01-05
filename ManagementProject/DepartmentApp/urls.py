from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_departmet,name="add_department"),
    path('show/',views.showdepartment,name="show_department"),
    path('update/<int:i>/',views.update_departmet,name="update_department"),
    path('delete/<int:i>/',views.delete_department,name="delete_department"),
]