from django.urls import path
from . import views

urlpatterns = [
    path('', views.coach_index, name='coach_index'),
    
    path('add_coordinator/', views.add_coordinator, name='add_coordinator'),
    path('add_events/', views.add_events, name='add_events'),
    path('add_inventory/', views.add_inventory, name="add_inventory"),
    
    path('view_coordinator/', views.view_coordinator, name='view_coordinator'),
    path('view_events/', views.view_events, name='view_events'),
    path('view_cricket_team/', views.view_cricket_team, name='view_cricket_team'),
    path('view_football_team/', views.view_football_team, name='view_football_team'),
    path('view_cricket/', views.view_cricket, name='view_cricket'),
    path('view_football/', views.view_football, name='view_football'),
    path('view_inventory/', views.view_inventory, name="view_inventory"),
    path('view_budget/', views.view_budget, name="view_budget"),
    path('view_sponsor/', views.view_sponsor, name="view_sponsor"),
    path('view_achievements/', views.view_achievements, name="view_achievements"),
    path('view_match_history/', views.view_match_history, name="view_match_history"),
    path('view_report/', views.view_report, name="view_report"),
    
    path('edit_coordinator/<id>', views.edit_coordinator, name='edit_coordinator'),
    path('edit_inventory/<id>', views.edit_inventory, name="edit_inventory"),
    path('edit_event/<id>', views.edit_event, name='edit_event'),
    
    
]
