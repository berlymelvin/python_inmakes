from django.urls import path

from movieapp import views
app_name='movieapp'

urlpatterns = [
    path('', views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('new-movie/', views.new_movie,name='new_movie'),
    path('edit-movie/<int:id>/', views.update_movie,name='update_movie'),
    path('delete-movie/<int:id>/',views.delete_movie,name='delete_movie'),
]