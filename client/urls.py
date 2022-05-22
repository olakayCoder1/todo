from django.urls import path
from . import views





urlpatterns = [ 
   # path('', views.welcome , name='welcome-page'),
    path('', views.homepage, name='home-page'),
    path('task/edit/<int:id>', views.edit_task, name="edit-task"),
    path('task/delet/<int:id>', views.delete_task, name="delete-task")
]