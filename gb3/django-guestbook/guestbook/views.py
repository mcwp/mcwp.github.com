from django.core.cache import cache
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from guestbook.forms import CreateGreetingForm
from guestbook.models import Greeting
from guestbook.models import State, Flower
import logging

MEMCACHE_GREETINGS = 'greetings'
MEMCACHE_STATES = 'states'

stash = """
                  <ul class="media-grid">
      	<h2>Five States</h2>
      	{% extends 'base2.html' %}
      	{% for state in states %}
      	<li>
      	  <a href="#">
      	    <!-- <img width="161" height="161" src={{ state.flower.picture }}/> -->
      	    <h1>{{ state.name }}</h1>
      	  </a>
      	</li>
      	{% endfor %}
      </ul><!-- end media-grid -->

	      {% if greeting.author %}
	      	<b>{{ greeting.author.username }}</b> wrote:
	      {% else %}
	      	An anonymous person wrote:
	      {% endif %}

"""


def list_states(request):
    states_q = State.objects.all()
    if len(states_q) >= 5:
        states = states_q[:5]
    else:
        states = []
    logging.info('list_states set states to %s', str(states))
    greetings = Greeting.objects.all().order_by('-date')[:10]
    cache.add(MEMCACHE_GREETINGS, greetings)
    return direct_to_template(request, 'guestbook/stateflower.html',
                              {'greetings': greetings,
                               'states': states,
                               'form': CreateGreetingForm()})

def list_flowers(request):
    greetings = Greeting.objects.all().order_by('-date')[:10]
    cache.add(MEMCACHE_GREETINGS, greetings)
    return direct_to_template(request, 'guestbook/stateflower.html',
                              {'greetings': greetings,
                               'form': CreateGreetingForm()})

def list_pairs(request):
    # List the flower/state pairs 
    states = State.objects.all()[:5]
    cache.add(MEMCACHE_STATES, states)
#    return direct_to_template(request, 'guestbook/answers.html',
    return direct_to_template(request, 'guestbook/stateflower.html',
                              {'states': states,
                               'form': CreateGreetingForm()})

def welcome_view(request):
    greetings = Greeting.objects.all().order_by('-date')[:10]
    cache.add(MEMCACHE_GREETINGS, greetings)
    return direct_to_template(request, 'guestbook/stateflower.html',
                              {'greetings': greetings,
                               'form': CreateGreetingForm()})

def list_greetings(request):
    greetings = cache.get(MEMCACHE_GREETINGS)
    if greetings is None:
        greetings = Greeting.objects.all().order_by('-date')[:10]
        cache.add(MEMCACHE_GREETINGS, greetings)
    return direct_to_template(request, 'guestbook/stateflower.html',
                              {'greetings': greetings,
                               'form': CreateGreetingForm()})

def create_greeting(request):
    if request.method == 'POST':
        form = CreateGreetingForm(request.POST)
        if form.is_valid():
            greeting = form.save(commit=False)
            if request.user.is_authenticated():
                greeting.author = request.user
            greeting.save()
            cache.delete(MEMCACHE_GREETINGS)
    return HttpResponseRedirect('/guestbook/')

def create_new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user must be active for login to work
            user.is_active = True
            user.save()
            return HttpResponseRedirect('/guestbook/')
    else:
        form = UserCreationForm()
    return direct_to_template(request, 'guestbook/user_create_form.html',
        {'form': form})
