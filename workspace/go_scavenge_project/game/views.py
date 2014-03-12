from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from game.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from game.models import UserProfile, Stat
from django.contrib.auth.models import User




from House import House, Game



def index(request):
    context = RequestContext(request)


    stats_list = Stat.objects.all()[:5]
    context_dict = {'boldmessage':"Survive?", 'stats': stats_list}
    

    return render_to_response('game/index.html', context_dict, context)


def about(request):
    return HttpResponse("Go Scavenge About Page")


def user_login(request):

    context = RequestContext(request)

    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/game/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your game account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('game/login.html', {}, context)
        
        
def register(request):
    context = RequestContext(request)
    
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
        
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()
            
            registered = True
        
        else:
            print user_form.errors, profile_form.errors
            
    else: 
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render_to_response(
        'game/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context)


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/game/')

def profile(request):
    context = RequestContext(request)

    individual_list = Stat.objects.filter(user=request.user)
    profile = UserProfile.objects.filter(user=request.user)
  

    context_dict = {'stats': individual_list, 'pa':profile[0].about, 'pp': profile[0].picture}




    return render_to_response('game/profile.html', context_dict, context)
    
def leaderboard(request):
    return HttpResponse("Go Scavenge About Page")
def play(request):
    return HttpResponse("Go Scavenge About Page")
def move(request):
    return HttpResponse("Go Scavenge About Page")
def stay(request):
    return HttpResponse("Go Scavenge About Page")

def gamescreen(request):
	context = RequestContext(request)
	mygame = Game()
	mygame.selectHouse(0)
	testText = mygame.report()
	survivors = testText[0]
	food = testText[1]
	ammo = testText[2]
	moves = testText[3]

	context_dict = {'food': food, 'ammo':ammo, 'moves': moves, 'survivors': survivors}
	return render_to_response('game/gamescreen.html',context_dict, context)
