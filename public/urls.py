from django.urls import path
from . import views

urlpatterns = [
    
    path('add_sponsor_pb/', views.add_sponsor_pb, name='add_sponsor_pb'),
    
    path('view_match_history_pb/', views.view_match_history_pb, name='view_match_history_pb'),
    path('view_achievements_pb/', views.view_achievements_pb, name='view_achievements_pb'),
    path('view_cricket_pb/', views.view_cricket_pb, name='view_cricket_pb'),
    path('view_football_pb/', views.view_football_pb, name='view_football_pb'),
    path('view_sponsor_pb/', views.view_sponsor_pb, name='view_sponsor_pb'),
    path('view_events_pb/', views.view_events_pb, name='view_events_pb'),
    
]