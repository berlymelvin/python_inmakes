from django.urls import path
from todoapp import views

app_name='todoapp'

urlpatterns = [
    path('', views.index,name='index'),
    path('delete/<int:id>/', views.delete_task,name='delete_task'),
    path('edit/<int:id>/',views.edit_task,name='edit_task'),
    path('cbvhome/',views.TodoListView.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.TodoDetailView.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.TodoUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TodoDeleteView.as_view(),name='cbvdelete'),
]