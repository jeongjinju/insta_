from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:id>/update/',views.update, name="update"),
    path('hashtags/<int:id>/', views.hashtags, name="hashtags"),
    path('<int:id>/likes/', views.likes, name="likes"),
    path('<int:id>/comment_create',views.comment_create, name="comment_create"),
    path('<int:post_id>/comment_delete/<int:comment_id>/',views.comment_delete, name="comment_delete"),
 
]
