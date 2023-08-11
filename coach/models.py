from django.db import models

class user_auth(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=True)
    user_type = models.CharField(max_length=100)
    status = models.IntegerField(null=True)
    name = models.CharField(max_length=298, null=True)

    def __str__(self):
        return self.username
    

class coordinator(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=14)
    sport_type = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    
class event(models.Model):
    event_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100, null=True)
    sport_type = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    coordinator = models.ForeignKey(coordinator, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name
    
    
class sponsor(models.Model):
    name = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100, null=True)
    details = models.CharField(max_length=289)
    date = models.DateField()

    def __str__(self):
        return self.name
    

class inventory(models.Model):
    item_name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    purchase_date = models.CharField(max_length=20)
    item_price = models.IntegerField()
    sponsor = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name
    

class achievements(models.Model):
    player_name = models.CharField(max_length=100, null=True)
    achievement = models.CharField(max_length=200)
    date = models.DateField()
    event_name = models.CharField(max_length=100, null=True)
    details = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return self.player_name
    
    
class cricket(models.Model):
    team_name = models.CharField(max_length=100)
    matches_played = models.IntegerField()
    matches_won = models.IntegerField(null=True)
    matches_lost = models.IntegerField(null=True)
    coordinator = models.ForeignKey(coordinator, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name
    
    
class cricket_performance(models.Model):
    player_name = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=10, null=True)
    contact_info = models.CharField(max_length=20, null=True)
    batting_style = models.CharField(max_length=100, null=True)
    bowling_style = models.CharField(max_length=100, null=True)
    matches_played = models.IntegerField(null=True)
    runs_scored = models.IntegerField(null=True)
    wickets_taken = models.IntegerField(null=True)
    highest_score = models.IntegerField(null=True)
    highest_wicket = models.IntegerField(null=True)
    team = models.ForeignKey(cricket, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.player_name
    

class football(models.Model):
    team_name = models.CharField(max_length=100)
    matches_played = models.IntegerField()
    matches_won = models.IntegerField(null=True)
    matches_lost = models.IntegerField(null=True)
    coordinator = models.ForeignKey(coordinator, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name
    
    
class football_performance(models.Model):
    player_name = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    contact_info = models.CharField(max_length=20, null=True)
    strong_foot = models.CharField(max_length=10, null=True)
    matches_played = models.IntegerField(null=True)
    goals_scored = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    highest_goal_score = models.IntegerField(null=True)
    red_cards = models.CharField(max_length=100, null=True)
    yellow_cards = models.CharField(max_length=100, null=True)
    team = models.ForeignKey(football, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.player_name



class budget(models.Model):
    total_spending = models.CharField(max_length=20)
    event_name =  models.CharField(max_length=267, null=True)
    date = models.DateField(null=True)
    location = models.CharField(max_length=300, null=True)

    def __str__(self):
        pass
    
    
class training(models.Model):
    team_name = models.CharField(max_length=100, null=True)
    details = models.CharField(max_length=300, null=True)
    reporting_time = models.CharField(max_length=10)
    location = models.CharField(max_length=60)
    coordinator = models.ForeignKey(coordinator, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name


class problem(models.Model):
    name = models.CharField(max_length=100)
    problem_details = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=20)
    date = models.DateField(null=True)
    recovery_status = models.CharField(max_length=20) 

    def __str__(self):
        return self.name
    

class history(models.Model):
    team_name = models.CharField(max_length=100)
    # sport_type =  models.CharField(max_length=20)
    event_name = models.CharField(max_length=300, null=True)
    opponent = models.CharField(max_length=60)
    final_score = models.CharField(max_length=60)
    opponent_score = models.CharField(max_length=100, null=True)
    result = models.CharField(max_length=100, null=True)
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name
    
    
class cricket_individual(models.Model):
    player = models.ForeignKey(cricket_performance, on_delete=models.CASCADE)
    runs_scored = models.IntegerField()
    wickets_taken = models.IntegerField()
    


class football_individual(models.Model):
    player = models.ForeignKey(football_performance, on_delete=models.CASCADE)
    goals_scored = models.IntegerField()
    assists = models.IntegerField()
    yellow_card = models.IntegerField()
    red_card = models.IntegerField()