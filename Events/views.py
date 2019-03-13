from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q 
from .models import Event
from datetime import date 
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect

#events=Event.objects.all().order_by('event_date')

def index(request):
    events=Event.objects.all().order_by('event_date')
    latest_events={ }
    latest_events = events.exclude (event_date__lt = date.today())
    #latest_events=latest_events.reverse()
    viewContext={'events':latest_events}
    return render(request,'Events/index.html',viewContext)

	

	
def search(request):
    events=Event.objects.all()
    latest_events={ }
    latest_events = events.exclude (event_date__lt = date.today())
    latest_events=latest_events.reverse()
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(event_name__icontains=query)| Q(event_date__icontains=query)| Q(event_organizer__icontains=query)

            results= latest_events.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'events/search.html', context)

        else:
            return render(request, 'events/search.html')

    else:
        return render(request, 'events/search.html')
 
	

def about(request):
     return render(request,'Events/about.html',)
