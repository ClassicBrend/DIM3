from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from game.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from game.models import UserProfile, Stat
from django.contrib.auth.models import User
from game.House import Game, House
import os




from House import House, Game



def index(request):
    context = RequestContext(request)


    stats_list = Stat.objects.order_by('-longest_session')[:5]
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
            context_dict = { 'badlogin':"Invalid login details"}
            return render_to_response("game/login.html", context_dict, context)

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

def loadgame(request):
    context = RequestContext(request)

    mygame = Game()

    loaded_data = mygame.unpickleData()

    context_dict = {"moves":loaded_data["moves"],"food":loaded_data["food"],"ammo":loaded_data["ammo"],"survivors":loaded_data["survivors"],"atHouse":loaded_data["atHouse"],"dayno":loaded_data["dayno"], "maxfood":loaded_data["maxfood"], "maxsurvivors":loaded_data["maxsurvivors"]}



    return render_to_response('game/gamescreen.html', context_dict, context)



@login_required
def gamescreen(request):
    context = RequestContext(request)

    mygame = Game()
    context_dict = {'test': "test"}
    if 'House1' in request.POST:
        mygame.selectHouse(0)
    if 'House2' in request.POST:
        mygame.selectHouse(1)
    if 'House3' in request.POST:
        mygame.selectHouse(2)
    if 'House4' in request.POST:
        mygame.selectHouse(3)
    if 'House5' in request.POST:
        mygame.selectHouse(4)
    prevMoves = int(request.POST.get("prevMoves") or 8)
    prevAmmo = int(request.POST.get("prevAmmo") or 0)
    prevSurvivors = int(request.POST.get("prevSurvivors") or 3)
    prevFood = int(request.POST.get("prevFood") or 0)
    currentHouse = int(request.POST.get("curHouse") or -1)
    currentDay = int(request.POST.get("dayno") or 0)
    maxSurvivors = int(request.POST.get("maxSurvivors") or -1)
    maxFood = int(request.POST.get("maxFood") or 0)
    mygame.updateData(prevMoves, prevFood, prevAmmo, prevSurvivors, currentHouse,currentDay, maxFood, maxSurvivors)
    mygame.inspectHouse()
    gameData = mygame.report()
    context_dict['survivors'] = gameData[0]
    context_dict['food'] = gameData[1]
    context_dict['ammo'] = gameData[2]
    context_dict['moves'] = gameData[3]
    context_dict['curHouse'] = gameData[4]
    context_dict['dayno'] = gameData[5]
    context_dict['maxFood'] = gameData[6]
    context_dict['maxSurvivors'] = gameData[7]
    if gameData[0] <= 0:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'go_scavenge_project.settings')

        profile = request.user.get_profile()

        if Stat.objects.filter(user=profile.user).count()==0:
            Stat.objects.get_or_create(user=profile.user, longest_session=gameData[5], max_survivors=gameData[7], supplies=gameData[6])
        else:
            s = Stat.objects.get(user=profile.user)
            if gameData[5] > s.longest_session:
                s.longest_session = gameData[5]
                s.max_survivors = gameData[7]
                s.supplies = gameData[6]
                s.save()



        return render_to_response('game/gameover.html', context_dict, context)
    return render_to_response('game/gamescreen.html',context_dict, context)

@login_required
def gameover(request):
    context = RequestContext(request)

    return render_to_response('game/gameover.html', context)
