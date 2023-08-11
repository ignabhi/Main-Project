from django.urls import path
from . import views

urlpatterns = [
    path('', views.athlete_index, name='athlete_index'),
    
    path('add_problem_at/', views.add_problem_at, name='add_problem_at'),
    
    path('view_events_at/', views.view_events_at, name='view_events_at'),
    path('view_training_at/', views.view_training_at, name='view_training_at'),
    path('view_achievement_at/', views.view_achievement_at, name='view_achievement_at'),
    path('view_problems_at/', views.view_problems_at, name='view_problems_at'),
    path('view_cricket_team_at/', views.view_cricket_team_at, name='view_cricket_team_at'),
    path('view_football_team_at/', views.view_football_team_at, name='view_football_team_at'),
    path('view_match_history_at/', views.view_match_history_at, name='view_match_history_at'),
    
    path('edit_problem_at/<id>', views.edit_problem_at, name='edit_problem_at'),
    
]