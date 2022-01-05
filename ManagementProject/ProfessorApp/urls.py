from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_professor,name="add_professor"),
    path('show/',views.showprofessor,name="show_professor"),
    path('update/<int:i>/',views.update_professor,name="update_professor"),
    path('delete/<int:i>/',views.delete_professor,name="delete_professor"),
]