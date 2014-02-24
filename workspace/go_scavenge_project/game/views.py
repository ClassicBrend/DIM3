from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    context = RequestContext(request)
    
    context_dict = {'boldmessage':"Survive?"}
    
    
    return render_to_response('game/index.html',context_dict,context)
    
def about(request):
    return HttpResponse("Go Scavenge About Page")
