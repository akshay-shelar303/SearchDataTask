from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_student,name="add_student"),
    path('show/',views.showstudent,name="show_student"),
    path('update/<int:i>/',views.update_student,name="update_student"),
    path('delete/<int:i>/',views.delete_student,name="delete_student"),
]