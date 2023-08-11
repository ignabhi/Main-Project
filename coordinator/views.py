from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import *
from coach.models import *
from django.utils import timezone
from django.db.models import Sum
from django.db.models import Max
from django.db.models import Avg
from django.db.models import F




# Create your views here.

def coordinator_index(request):
    context = {}
    context["Coordinator"] = True
    context["title"] = "Coordinator Home"
    context["name"] = user_auth.objects.get(id = request.session["lid"]).name
    
    return render(request,'coordinator/coordinator-index.html', context)


def view_cricket_team_co(request):
    context = {}
    context["Cricket"] = True
    context["title"] = "Cricket Teams"
    context['data'] = cricket.objects.all()
    context['count'] = cricket_performance.objects.all().count()
    
    return render(request,'coordinator/view-cricket-team.html', context)


def add_player_cricket_co(request, id):
    context={}
    context["Add Players"] = True
    context["title"] = "Add Players" 
    if request.method == 'POST':
        player_name = request.POST['player_name']
        role = request.POST['role']
        contact_info = request.POST['contact_info']
        batting = request.POST['batting']
        bowling = request.POST['bowling']
        
        cricket_performance.objects.create(player_name = player_name, role = role, contact_info = contact_info, batting_style = batting, bowling_style = bowling, team_id = id)
        return HttpResponse('<script>alert("Player Added");window.location="/coordinator/view_cricket_team_co"</script>')
    else:
        return render(request,'coordinator/add-new-player-cricket.html', context)
    
    
def add_player_football_co(request, id):
    context={}
    context["Add Players"] = True
    context["title"] = "Add Players" 
    if request.method == 'POST':
        player_name = request.POST['player_name']
        position = request.POST['position']
        contact_info = request.POST['contact_info']
        strong_foot = request.POST['strong_foot']
        
        football_performance.objects.create(player_name = player_name, position = position, contact_info = contact_info, strong_foot = strong_foot, team_id = id)
        return HttpResponse('<script>alert("Player Added");window.location="/coordinator/view_football_team_co"</script>')
    else:
        return render(request,'coordinator/add-new-player-football.html', context)
        

def view_football_team_co(request):
    context = {}
    context["Cricket"] = True
    context["title"] = "Cricket Teams"
    context['data'] = football.objects.all()
    context['count'] = football_performance.objects.all().count()
    
    return render(request,'coordinator/view-football-team.html', context)


def add_training_co(request):
    context = {}
    context["Training"] = True
    context["title"] = "Add Training"
    context['filter'] = cricket.objects.all()
    context['filter2'] = football.objects.all()
    context["filter3"] = coordinator.objects.all()
    
    if request.method == 'POST':
        team_name = request.POST['team_name']
        details = request.POST['details']
        time = request.POST['time']
        location = request.POST['location']
        coordinator_id = request.POST['coordinator_id']
        
        training.objects.create(team_name = team_name, details = details, reporting_time = time, location = location, coordinator_id = coordinator_id)
        return HttpResponse('<script>alert("Training Added");window.location="/coordinator/view_training_co"</script>')
    else: 
        return render(request,'coordinator/add-training.html', context)
    
    
def view_training_co(request):
    context = {}
    context["Training"] = True
    context["title"] = "Training"
    context['data'] = training.objects.all()
    return render(request,'coordinator/view-training.html', context)


def edit_training_co(request, id):
    context = {}
    context["Training"] = True
    context["title"] = "Edit Training"
    context["filter3"] = coordinator.objects.all()
    context['update'] = training.objects.get(id = id)
    
    if request.method == 'POST':
        details = request.POST['details']
        time = request.POST['time']
        location = request.POST['location']
        coordinator_id = request.POST['coordinator_id']
        
        value = training.objects.get(id = id)
        value.details = details
        value.time = time
        value.location = location
        value.coordinator_id = coordinator_id
        value.save()
        
        return HttpResponse('<script>alert("Record Updated");window.location="/coordinator/view_training_co"</script>')
    
    return render(request,'coordinator/edit-training.html', context)


def add_achievements_co(request):
    context = {}
    context["Achievement"] = True
    context["title"] = "Add Achievements"
    context['filter'] = event.objects.filter(event_type = "Tournament")
    context["filter2"] = cricket_performance.objects.all()
    context["filter3"] = football_performance.objects.all()
    
    if request.method == 'POST':
        achievement = request.POST['achievement']
        date = request.POST['date']
        player_name = request.POST['player_name']
        details = request.POST['details']
        event_name = request.POST['event_name']
        achievements.objects.create(player_name = player_name, achievement = achievement, date = date, event_name = event_name, details = details)
        return HttpResponse('<script>alert("Achievement Added");window.location="/coordinator/view_achievement_co"</script>')
    
    else:
        return render(request,'coordinator/add-achievements.html', context)
    
    

def view_achievement_co(request):
    context = {}
    context["Achievements"] = True
    context["title"] = "Achievements"
    context['data'] = achievements.objects.all()
    
    return render(request,'coordinator/view-achievements.html', context)


def add_match_history_co(request):
    context = {}
    context["Match History"] = True
    context["title"] = "Add Match History"
    context['filter'] = cricket.objects.all()
    context['filter2'] = football.objects.all()
    context['filter3'] = event.objects.filter(event_type = "Tournament")
    
    if request.method == 'POST':
        team_name = request.POST['team_name']
        event_name = request.POST['event_name']
        opponent = request.POST['opponent']
        final_score = request.POST['final_score']
        final_score_opponent = request.POST['final_score_opponent']
        result = request.POST['result']
        date = request.POST['date']
        location = request.POST['location']            

        history.objects.create(team_name = team_name, event_name = event_name, opponent = opponent, final_score = final_score, opponent_score = final_score_opponent, result = result, date = date, location = location)
        if cricket.objects.filter(team_name = team_name).exists():
            cricket.objects.filter(team_name = team_name).update(matches_played = F('matches_played') + 1)
            if result == "Win":
                cricket.objects.filter(team_name = team_name).update(matches_won = F('matches_won') + 1)
            elif result == "Lose":
                cricket.objects.filter(team_name = team_name).update(matches_lost = F('matches_lost') + 1)
                
        elif football.objects.filter(team_name = team_name).exists():
            football.objects.filter(team_name = team_name).update(matches_played = F('matches_played') + 1)
            if result == "Win":
                cricket.objects.filter(team_name = team_name).update(matches_won = F('matches_won') + 1)
            elif result == "Lose":
                cricket.objects.filter(team_name = team_name).update(matches_lost = F('matches_lost') + 1)
            
        return HttpResponse('<script>alert("Match History Added");window.location="/coordinator/view_match_history_co"</script>')

    else:
        return render(request,'coordinator/add-match-history.html', context)
    
    
def view_match_history_co(request):
    context = {}
    context["Match History"] = True
    context["title"] = "Match History"
    context['data'] = history.objects.all()
    
    return render(request,'coordinator/view-match-history.html', context)


def add_budget_co(request):
    context = {}
    context["Add Budget"] = True
    context["title"] = "Add Budget"
    context["filter"] = event.objects.all()
    if request.method == 'POST':
        event_name = request.POST['event_name']
        spending = request.POST['spending']
        date = request.POST['date']
        location = request.POST['location']
        budget.objects.create(event_name = event_name, total_spending = spending, date = date, location = location)
        return HttpResponse('<script>alert("Match History Added");window.location="/coordinator/view_budget_co "</script>')
        
    else:
        return render(request, 'coordinator/add-budget.html', context)


def view_budget_co(request):
    context = {}
    context["Budget"] = True
    context["title"] = "Budget"
    context["data"] = budget.objects.all()
    
    return render(request, 'coordinator/view-budget.html', context)


def view_events_co(request):
    context = {}
    context["Events"] = True
    context["title"] = "Events"
    context["data"] = event.objects.all()
    
    return render(request, 'coordinator/view-events-co.html', context)


def view_problem_co(request):
    context = {}
    context["Problems"] = True
    context["title"] = "Problems"
    context["data"] = problem.objects.all()
    
    return render(request, 'coordinator/view-problems-co.html', context)


def view_cricket_players_co(request, id):
    context = {}
    context["Cricket Team"] = True
    context["title"] = "Cricket Team"
    context["data"] = cricket_performance.objects.filter(team_id = id)
        
    return render(request, 'coordinator/view-cricket-players.html', context)


def view_football_players_co(request, id):
    context = {}
    context["Football Team"] = True
    context["title"] = "Football Team"
    context["data"] = football_performance.objects.filter(team_id = id)
    
    return render(request, 'coordinator/view-football-players.html', context)


def view_cricket_performance_co(request):
    context = {}
    context["Cricket"] = True
    context["title"] = "Cricket Performance"
    context["data"] = cricket_performance.objects.all()
    
    return render(request, 'coordinator/view-cricket-performance.html', context)


def edit_cricket_performance_co(request, id):
    context = {}
    context["Cricket"] = True
    context["title"] = "Cricket Performance"
    context["update"] = cricket_performance.objects.get(id = id)
    
    if request.method == 'POST':
        role = request.POST['role']
        # matches = request.POST['matches']
        # runs = request.POST['runs']
        # wickets = request.POST['wickets']
        # highest_runs = request.POST['highest_runs']
        # highest_wicket = request.POST['highest_wicket']
        
        value = cricket_performance.objects.get(id = id)
        
        value.role = role
        # value.matches_played = matches
        # value.runs_scored = runs
        # value.highest_score = highest_runs
        # value. highest_wicket = highest_wicket
        # value.wickets_taken = wickets
        value.save()
        
        return HttpResponse('<script>alert("Record Updated");window.location="/coordinator/view_cricket_performance_co"</script>')
    
    return render(request, 'coordinator/edit-cricket-performance.html', context)


def view_football_performance_co(request):
    context = {}
    context["Football"] = True
    context["title"] = "Football Performance"
    context["data"] = football_performance.objects.all()
    
    return render(request, 'coordinator/view-football-performance.html', context)


def edit_football_performance_co(request, id):
    context = {}
    context["Football"] = True
    context["title"] = "Football Performance"
    context["update"] = football_performance.objects.get(id = id)
    if request.method == 'POST':
        position = request.POST['position']
        matches = request.POST['matches']
        goal = request.POST['goal']
        assists = request.POST['assists']
        highest_goal = request.POST['highest_goal']
        yellow = request.POST['yellow']
        red = request.POST['red']
        
        value = football_performance.objects.get(id = id)
        value.position = position
        value.matches_played = matches
        value.goals_scored = goal
        value.assists = assists
        value.highest_goal_score = highest_goal
        value.red_cards = red
        value.yellow_cards = yellow
        value.save()
        
        return HttpResponse('<script>alert("Record Updated");window.location="/coordinator/view_football_performance_co"</script>')
    
    return render(request, 'coordinator/edit-football-performance.html', context)



def add_player_performance_cricket(request):
    context = {}
    context["Player"] = True
    context["title"] = "Player Performance"
    context["filter"] = cricket_performance.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        runs = request.POST['runs']
        wickets = request.POST['wickets']
        
        cricket_individual.objects.create(player_id = name, runs_scored = runs, wickets_taken = wickets)
        return HttpResponse('<script>alert("Record Added");window.location="/coordinator/view_cricket_performance_co"</script>')
    
    return render(request, 'coordinator/add-player-performance-cricket.html', context)



def view_player_performance_cricket(request, id):
    context = {}
    context["Player"] = True
    context["title"] = "Player Performance"
    
    context["name"] = cricket_performance.objects.get(id = id)
    context["data"] = cricket_individual.objects.filter(player_id = id)
    context["total_matches"] = cricket_individual.objects.filter(player_id = id).count()
    context["loop"] = cricket_individual.objects.filter(player_id = id)
    context["runs"] = cricket_individual.objects.filter(player_id = id).aggregate(Sum('runs_scored'))['runs_scored__sum']
    context["wickets"] = cricket_individual.objects.filter(player_id = id).aggregate(Sum('wickets_taken'))['wickets_taken__sum']
    context["highest_run"] = cricket_individual.objects.filter(player_id = id).aggregate(max_value=Max('runs_scored'))['max_value']
    context["highest_wicket"] = cricket_individual.objects.filter(player_id = id).aggregate(max_value=Max('wickets_taken'))['max_value']
    context["avg_runs"] = cricket_individual.objects.filter(player_id = id).aggregate(avg_value=Avg('runs_scored'))['avg_value']
    context["avg_wickets"] = cricket_individual.objects.filter(player_id = id).aggregate(avg_value=Avg('wickets_taken'))['avg_value']


    return render(request, 'coordinator/view-individual-cricket.html', context)



def add_player_performance_football(request):
    context = {}
    context["Player"] = True
    context["title"] = "Player Performance"
    context["filter"] = football_performance.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        goal = request.POST['goal']
        assists = request.POST['assists']
        yellow_card = request.POST['yellow']
        red_card = request.POST['red']
        
        
        football_individual.objects.create(player_id = name, goals_scored = goal, assists = assists, yellow_card = yellow_card, red_card = red_card)
        return HttpResponse('<script>alert("Record Added");window.location="/coordinator/view_football_performance_co"</script>')
    
    return render(request, 'coordinator/add-player-performance-football.html', context)



def view_player_performance_football(request, id):
    context = {}
    context["Player"] = True
    context["title"] = "Player Performance"
    
    context["name"] = football_performance.objects.get(id = id)
    context["data"] = football_individual.objects.filter(player_id = id)
    context["total_matches"] = football_individual.objects.filter(player_id = id).count()
    context["loop"] = football_individual.objects.filter(player_id = id)
    context["goals"] = football_individual.objects.filter(player_id = id).aggregate(Sum('goals_scored'))['goals_scored__sum']
    context["assists"] = football_individual.objects.filter(player_id = id).aggregate(Sum('assists'))['assists__sum']
    context["yellow_card"] = football_individual.objects.filter(player_id = id).aggregate(Sum('yellow_card'))['yellow_card__sum']
    context["red_card"] = football_individual.objects.filter(player_id = id).aggregate(Sum('red_card'))['red_card__sum']
    context["highest_goal"] = football_individual.objects.filter(player_id = id).aggregate(max_value=Max('goals_scored'))['max_value']
    context["highest_assists"] = football_individual.objects.filter(player_id = id).aggregate(max_value=Max('assists'))['max_value']
    context["avg_goals"] = football_individual.objects.filter(player_id = id).aggregate(avg_value=Avg('goals_scored'))['avg_value']
    

    return render(request, 'coordinator/view-individual-football.html', context)
