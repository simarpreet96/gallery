from django.urls import path
from . import views
urlpatterns = [
     path('', views.allposts, name='allposts'),
     path('add/', views.add_post, name='add_post'),
     path('post_people/', views.post_people, name='post_people'),
     path('post_places/', views.post_places, name='post_places'),
     path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

     path('places/<int:pk>/comment/', views.places_comment, name='places_comment'),

     path('people_comment/<int:pk>/comment/', views.people_comment, name='people_comment'),
     path('signup/', views.signup, name='signup'),
     path('Category/', views.Category, name='Category'),
     path('people/', views.people, name='people'),
     path('places/', views.places, name='places'),
     path('posts/', views.posts, name='posts'),
     path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
     path('people_detail/<int:id>', views.people_detail, name='people_detail'),
     path('places_detail/<int:pk>', views.places_detail, name='places_detail'),
     


     


     




     
]