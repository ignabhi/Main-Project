from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import *
from coach.models import *
from django.db.models import Sum

# Create your views here.
#----------------------------------------------------------MAIN START----------------------------------------------------------------

def index(request):
    context = {}
    context["Public Home"] = True
    context["title"] = "Dashboard"
    
    return render(request,'index.html', context)


def login_auth(request):
    context = {}
    context['Login'] = True
    context["title"] = "Login"
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username and password:
            if user_auth.objects.filter(username = username, password = password).exists():
                object = user_auth.objects.get(username = username, password =  password)
                request.session['lid'] = object.id
                if object.user_type == "coach":
                    return redirect("/coach")
                elif object.user_type == "coordinator": 
                    return redirect("/coordinator")
                elif object.user_type == "athlete":
                    check = object.name
                    if cricket_performance.objects.filter(player_name = check).exists() or football_performance.objects.filter(player_name = check).exists():
                        return redirect("/athlete")
                    else:
                        return HttpResponse('<script>alert("You are not Selected in Any Team Yet");window.location="/login"</script>')
                else:
                    return HttpResponse('<script>alert("Please provide a Valid Username or Password or User does not Exists");window.location="/login"</script>')
            else:
                    return HttpResponse('<script>alert("Please provide a Valid Username or Password or User does not Exists");window.location="/login"</script>')
        else:
                return HttpResponse('<script>alert("Please provide a Valid Username or Password or User does not Exists");window.location="/login"</script>')
    else:
        return render(request, 'pages-login.html')

    
def register(request):
    context = {}
    context['Register'] = True
    context["title"] = "Register"
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        password = request.POST["password"]
        user_auth.objects.create(name = name, username = username, password = password, user_type = "athlete")
        
        return HttpResponse('<script>alert("Registered Successfully");window.location="/login"</script>')
    
    return render(request,'pages-register.html', context)

#----------------------------------------------------------MAIN END------------------------------------------------------------------


#---------------------------------------------------------COACH START----------------------------------------------------------------

def coach_index(request):
    context = {}
    context["Coach"] = True
    context["title"] = "Dashboard"
    context["name"] = user_auth.objects.get(id = request.session["lid"]).name
    
    return render(request,'coach/coach-index.html', context)

def add_coordinator(request):
    context = {}
    context["Coordinator"] = True
    context["title"] = "Add Coordinator"
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact_info = request.POST['contact_info']
        sport_type = request.POST['sport_type']
        # email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if user_auth.objects.filter(username=username).exists():
            return HttpResponse('<script>alert("Username Already Exists");window.location="/coach/add_coordinator"</script>')
        else:
            coordinator.objects.create(name = first_name+" "+last_name, contact_info = contact_info, sport_type = sport_type, status = "Free")
            user_auth.objects.create(username = username, password = password, user_type = "coordinator", name = first_name+" "+last_name)
            return HttpResponse('<script>alert("Coordinator Saved");window.location="/coach/view_coordinator"</script>')
    else:
        return render(request,'coach/add-coordinator.html', context)


def view_coordinator(request):
    context = {}
    context["Coordinator"] = True
    context["title"] = "Coordinators"
    context['data'] = coordinator.objects.all()
    
    return render(request,'coach/view-coordinator.html',context)


def edit_coordinator(request, id):
    context = {}
    context["Coordinator"] = True
    context["title"] = "Edit Coordinators"
    context["update"] = coordinator.objects.get(id = id)
    if request.method == 'POST':
        contact_info = request.POST['contact_info']
        sport_type = request.POST['sport_type']
        status = request.POST['status']
        
        value = coordinator.objects.get(id = id)
        value.contact_info = contact_info
        value.sport_type = sport_type
        value.status = status
        value.save()
        
        return HttpResponse('<script>alert("Record Updated");window.location="/coach/view_coordinator"</script>')
    
    return render(request,'coach/edit-coordinator.html',context)
    

def add_events(request):
    context = {}
    context["Events"] = True
    context["title"] = "Add Event"
    context['filter']=coordinator.objects.filter(status = "Free")
    
    if request.method == 'POST':
        event_name = request.POST['event_name']
        event_type = request.POST['event_type']
        sport_type = request.POST['sport_type']
        date = request.POST['date']
        time = request.POST['time']
        location = request.POST['location']
        coordinator_id=request.POST['coordinator_id']
        event.objects.create(event_name = event_name,event_type = event_type, sport_type = sport_type, date = date, time = time, location = location,coordinator_id = coordinator_id)
        
        return HttpResponse('<script>alert("Event Added");window.location="/coach/view_events"</script>')
    else:
        return render(request,'coach/add-events.html', context)


def view_events(request):
    context = {}
    context["Event"] = True
    context["title"] = "Events"
    context['data'] = event.objects.all()
    context['filter'] = coordinator.objects.filter(status="Free")
    
    return render(request,'coach/view-events.html', context)


def edit_event(request, id):
    context = {}
    context["Event"] = True
    context["title"] = "Edit Event"
    context['filter'] = coordinator.objects.all()
    context["update"] = event.objects.get(id = id)
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        location = request.POST['location']
        coordinator_id=request.POST['coordinator_id']
        
        value = event.objects.get(id = id)
        value.date = date
        value.time = time
        value.location = location
        value.coordinator_id = coordinator_id
        value.save()
        return HttpResponse('<script>alert("Record Updated");window.location="/coach/view_events"</script>')
        
    return render(request,'coach/edit-events.html',context)


def view_cricket_team(request):
    context = {}
    context["Cricket Team"] = True
    context["title"] = "Cricket Team"
    context['data'] = cricket.objects.all()
    context['filter'] = coordinator.objects.filter(status = "Free", sport_type = "Cricket")
    
    if request.method == "POST":
        team_name = request.POST['team_name']
        coordinator_id = request.POST['coordinator_id']
    
        cricket.objects.create(team_name = team_name, matches_played = 0, matches_won = 0, matches_lost = 0, coordinator_id = coordinator_id)
        coordinator_update=coordinator.objects.get(id = coordinator_id)
        coordinator_update.status="Assigned"
        coordinator_update.save()
        
        return HttpResponse('<script>alert("Team Added");window.location="/coach/view_cricket_team"</script>')
    else:
        return render(request,'coach/view-cricket-team.html', context)


def view_football_team(request):
    context = {}
    context["Football Team"] = True
    context["title"] = "Football Team"
    context['data'] = football.objects.all()
    context['filter'] = coordinator.objects.filter(status = "Free", sport_type = "Football")
    
    if request.method == "POST":
        team_name = request.POST['team_name']
        coordinator_id = request.POST['coordinator_id']
    
        football.objects.create(team_name = team_name, matches_played = 0, matches_won = 0, matches_lost = 0, coordinator_id = coordinator_id)
        coordinator_update=coordinator.objects.get(id = coordinator_id)
        coordinator_update.status="Assigned"
        coordinator_update.save()
        
        return HttpResponse('<script>alert("Team Added");window.location="/coach/view_football_team"</script>')
    else: 
        return render(request,'coach/view-football-team.html', context)


def view_cricket(request):
    context = {}
    context["Cricket"] = True
    context["title"] = "Cricket"
    context['data'] = cricket_performance.objects.all()
    
    return render(request, 'coach/view-cricket.html', context)


def view_football(request):
    context = {}
    context["Football"] = True
    context["title"] = "Football"
    context['data'] = football_performance.objects.all()
    
    return render(request, 'coach/view-football.html', context)


def add_inventory(request):
    context = {}
    context["Inventory"] = True
    context["title"] = "Add Inventory Items"
    
    if request.method == "POST":
        item_name = request.POST['item_name']
        quantity = request.POST['quantity']
        status = request.POST['status']
        date = request.POST['date']
        price = request.POST['price']
        sponsor = request.POST['sponsor']
        
        inventory.objects.create(item_name = item_name, quantity = quantity, status = status, purchase_date = date, item_price = price, sponsor = sponsor)
        return HttpResponse('<script>alert("Inventory Item Added");window.location="/coach/view_inventory"</script>')
    else:
        return render(request,'coach/add-inventory.html', context)


def view_inventory(request):
    context = {}
    context["Inventory"] = True
    context["title"] = "Inventory Items"
    context['data'] = inventory.objects.all()
    
    return render(request,'coach/view-inventory.html', context)


def edit_inventory(request, id):
    context = {}
    context["Inventory"] = True
    context["title"] = "Edit Inventory"
    context["update"] = inventory.objects.get(id = id)
    if request.method == "POST":
        status = request.POST['status']
        value = inventory.objects.get(id = id)
        value.status = status
        value.save()
        
        return HttpResponse('<script>alert("Record Updated");window.location="/coach/view_inventory"</script>')
    
    return render(request,'coach/edit-inventory.html', context)


def view_budget(request):
    context = {}
    context["Budget"] = True
    context["title"] = "Budget"
    context["data"] = budget.objects.all()
    
    return render(request,'coach/view-budget.html', context)


def view_sponsor(request):
    context = {}
    context["Sponsor"] = True
    context["title"] = "Sponsors"
    context["data"] = sponsor.objects.all()
    
    return render(request,'coach/view-Sponsor.html', context)


def view_achievements(request):
    context = {}
    context["Achievements"] = True
    context["title"] = "Achievements"
    context['data'] = achievements.objects.all()
    
    return render(request,'coach/view-achievements.html', context)


def view_match_history(request):
    context = {}
    context["Match History"] = True
    context["title"] = "Match History"
    context['data'] = history.objects.all()
    
    return render(request,'coach/view-match-history.html', context)


def view_report(request):
    context = {}
    context["Reports"] = True
    context["title"] = "Reports"
    context["data"] = cricket.objects.all().count()
    context["data2"] = football.objects.all().count()
    context["data24"] = cricket.objects.all().count() + football.objects.all().count()
    context["data3"] = event.objects.filter(event_type = "Selection").count()
    context["data4"] = event.objects.filter(event_type = "Tournament").count()
    context["data25"] = event.objects.all().count()
    context["data5"] = achievements.objects.all().count()
    context["data6"] = coordinator.objects.all().count()
    context["data7"] = coordinator.objects.filter(status = "Free").count()
    context["data8"] = coordinator.objects.filter(status = "Assigned").count()
    context["data9"] = inventory.objects.all().count()
    context["data10"] = inventory.objects.filter(status="Good").count()
    context["data11"] = inventory.objects.filter(status="Damaged").count()
    context["data12"] = inventory.objects.filter(status="Broken").count()
    context["data13"] = cricket_performance.objects.all().count()
    context["data14"] = football_performance.objects.all().count()
    context["data15"] = cricket_performance.objects.all().count() + football_performance.objects.all().count()
    context["data16"] = problem.objects.all().count()
    context["data17"] = sponsor.objects.all().count()
    context["data18"] = history.objects.filter(result = "Win").count()
    context["data19"] = history.objects.filter(result = "Lose").count()
    context["data20"] = history.objects.filter(result = "Draw").count()
    context["data21"] = history.objects.all().count()
    context["data22"] = training.objects.all().count()
    

    context["data23"] = budget.objects.aggregate(Sum('total_spending'))
    
    return render(request,'coach/view-reports.html', context)

    

#---------------------------------------------------------COACH END------------------------------------------------------------------




