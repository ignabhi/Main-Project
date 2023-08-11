from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import *
from coach.models import *

# Create your views here.

def athlete_index(request):
    context = {}
    context["Athlete"] = True
    context["title"] = "Athlete Home"
    context["name"] = user_auth.objects.get(id = request.session["lid"]).name
    
    return render(request,'athlete/athlete-index.html', context)


def add_problem_at(request):
    context = {}
    context["Add Problem"] = True
    context["title"] = "Add Problem"
    context["filter"] = cricket_performance.objects.all()
    context["filter2"] = football_performance.objects.all()
    
    if request.method == "POST":
        player_name = request.POST['player_name']
        details = request.POST['details']
        contact = request.POST['contact']
        date = request.POST['date']
        ex_date = request.POST['ex_date']
        
        problem.objects.create(name = player_name, problem_details = details, contact_info = contact, date = date, recovery_status = ex_date)
        return HttpResponse('<script>alert("Problem Added");window.location="/athlete/view_problems_at"</script>')
    else:
        return render(request, 'athlete/add-problem-at.html', context)
    
    
def view_problems_at(request):
    context = {}
    context["Problems"] = True
    context["title"] = "Problems"
    context['data'] = problem.objects.all()
    context["filter"] = cricket_performance.objects.all()
    context["filter2"] = football_performance.objects.all()
    
    return render(request,'athlete/view-problem-at.html', context)


def edit_problem_at(request, id):
    context = {}
    context["Add Problem"] = True
    context["title"] = "Edit Problem"
    context["update"] = problem.objects.get(id = id)
    
    if request.method == "POST":
        ex_date = request.POST['ex_date']
        value = problem.objects.get(id = id)
        value.recovery_status = ex_date
        value.save()
        return HttpResponse('<script>alert("Record Updated");window.location="/athlete/view_problems_at"</script>')
    
    return render(request, 'athlete/edit-problem-at.html', context)


def view_cricket_team_at(request):
    context = {}
    context["Cricket Team"] = True
    context["title"] = "Cricket Team"
    context["data"] = cricket_performance.objects.all()
    
    return render(request, 'athlete/view-cricket-at.html', context)


def view_football_team_at(request):
    context = {}
    context["Football Team"] = True
    context["title"] = "Football Team"
    context["data"] = football_performance.objects.all()
    
    return render(request, 'athlete/view-football-at.html', context)


def view_events_at(request):
    context = {}
    context["Event"] = True
    context["title"] = "Events"
    context['data'] = event.objects.all()
    
    return render(request,'athlete/view-events-at.html', context)


def view_training_at(request):
    context = {}
    context["Training"] = True
    context["title"] = "Training"
    context['data'] = training.objects.all()
    
    return render(request,'athlete/view-training-at.html', context)


def view_achievement_at(request):
    context = {}
    context["Achievements"] = True
    context["title"] = "Achievements"
    context['data'] = achievements.objects.all()
    
    return render(request,'athlete/view-achievements-at.html', context)


def view_match_history_at(request):
    context = {}
    context["Match History"] = True
    context["title"] = "Match History"
    context['data'] = history.objects.all()
    
    return render(request, 'athlete/view-match-history-at.html', context)