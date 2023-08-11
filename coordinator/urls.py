from django.urls import path
from . import views

urlpatterns = [
    path('', views.coordinator_index, name='coordinator_index'),
    
    path('add_player_cricket_co/<id>', views.add_player_cricket_co, name='add_player_cricket_co'),
    path('add_player_football_co/<id>', views.add_player_football_co, name='add_player_football_co'),
    path('add_training_co/', views.add_training_co, name='add_training_co'),
    path('add_achievements_co/', views.add_achievements_co, name='add_achievements_co'),
    path('add_match_history_co/', views.add_match_history_co, name='add_match_history_co'),
    path('add_budget_co/', views.add_budget_co, name='add_budget_co'),
    
    path('view_cricket_team_co/', views.view_cricket_team_co, name='view_cricket_team_co'),
    path('view_football_team_co/', views.view_football_team_co, name='view_football_team_co'),
    path('view_training_co/', views.view_training_co, name='view_training_co'),
    path('view_achievement_co/', views.view_achievement_co, name='view_achievement_co'),
    path('view_match_history_co/', views.view_match_history_co, name='view_match_history_co'),
    path('view_budget_co/', views.view_budget_co, name='view_budget_co'),
    path('view_events_co/', views.view_events_co, name='view_events_co'),
    path('view_problem_co/', views.view_problem_co, name='view_problem_co'),
    path('view_cricket_players_co/<id>', views.view_cricket_players_co, name='view_cricket_players_co'),
    path('view_football_players_co/<id>', views.view_football_players_co, name='view_football_players_co'),
    path('view_cricket_performance_co', views.view_cricket_performance_co, name='view_cricket_performance_co'),
    path('view_football_performance_co', views.view_football_performance_co, name='view_football_performance_co'),
    
    path('edit_training_co/<id>', views.edit_training_co, name='edit_training_co'),
    path('edit_cricket_performance_co/<id>', views.edit_cricket_performance_co, name='edit_cricket_performance_co'),
    path('edit_football_performance_co/<id>', views.edit_football_performance_co, name='edit_football_performance_co'),
    
    path('add_player_performance_cricket/', views.add_player_performance_cricket, name='add_player_performance_cricket'),
    path('view_player_performance_cricket/<id>', views.view_player_performance_cricket, name='view_player_performance_cricket'),
    
    path('add_player_performance_football/', views.add_player_performance_football, name='add_player_performance_football'),
    path('view_player_performance_football/<id>', views.view_player_performance_football, name='view_player_performance_football'),
    
    
]