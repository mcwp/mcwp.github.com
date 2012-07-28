from django.db import models
from django.contrib.auth.models import User

class Greeting(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Flower(models.Model):
    picture = models.TextField()
#    state = models.ForeignKey(State)
    name = models.TextField()

class State(models.Model):
    name = models.CharField(max_length=30)
#    flower = models.ForeignKey(Flower)


    

    # add a fixture to initialize just 5 flowers and states
    # see if the admin shell works with manage.py or not
    

        
