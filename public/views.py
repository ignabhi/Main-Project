from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import *
from coach.models import *
from django.utils import timezone

# Create your views here.
def view_match_history_pb(request):
    context = {}
    context["Match History"] = True
    context["title"] = "Match History"
    context['data'] = history.objects.all()
    
    return render(request, 'view-match-history-pb.html', context)


def view_achievements_pb(request):
    context = {}
    context["Achievements"] = True
    context["title"] = "Achievements"
    context['data'] = achievements.objects.all()
    
    return render(request, 'view-achievements-pb.html', context)


def view_cricket_pb(request):
    context = {}
    context["Cricket"] = True
    context["title"] = "Cricket"
    context['data'] = cricket_performance.objects.all()
    
    return render(request, 'view-cricket-pb.html', context)


def view_football_pb(request):
    context = {}
    context["Football"] = True
    context["title"] = "Football"
    context['data'] = football_performance.objects.all()
    
    return render(request, 'view-football-pb.html', context)


def add_sponsor_pb(request):
    context = {}
    context["Sponsor"] = True
    context["title"] = " Add Supporters"
    
    if request.method == 'POST':
        name = request.POST['name']
        details = request.POST['details']
        current_date = timezone.now().date()
        
        sponsor.objects.create(name = name, details = details, date = current_date)
        return HttpResponse('<script>alert("Sponsor Added");window.location="/public/view_sponsor_pb"</script>')
    else:
        return render(request, 'add-sponsor-pb.html', context)


def view_sponsor_pb(request):
    context = {}
    context["Sponsor"] = True
    context["title"] = "Supporters"
    context["data"] = sponsor.objects.all()
    
    return render(request, 'view-supporters-pb.html', context)


def view_events_pb(request):
    context = {}
    context["Events"] = True
    context["title"] = "Events"
    context["data"] = event.objects.all()
    
    return render(request, 'view-events-pb.html', context)
    