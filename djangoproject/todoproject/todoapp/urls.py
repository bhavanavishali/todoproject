from . import views
from django.urls import path
app_name = 'todoapp'

urlpatterns = [
    path('',views.tasks,name= 'tasks'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
    # path('cbv',views.Tasklistview.as_view(),name='cbv'),
    
]