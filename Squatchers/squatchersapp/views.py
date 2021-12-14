from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting, Reporter

def indexPageView(request) :
    return render(request, 'squatchersapp/index.html')

def sightingsPageView(request) :
    sightings = Sighting.objects.all()
    context = {
        'sightings' : sightings
    }
    return render(request, 'squatchersapp/sightings.html', context)

def editSightingPageView(request, id):
    data = Sighting.objects.get(id=id)
    context = {
        'sighting' : data
    }
    return render(request, 'squatchersapp/editSighting.html', context)

def DeleteSightingPageView(request, id):
    data = Sighting.objects.get(id=id)
    data.delete()
    return sightingsPageView(request)

def aboutPageView(request) :
    return render(request, 'squatchersapp/about.html')

def sightingDetailsPageView(request) :
    return render(request, 'squatchersapp/sightingdetails.html')

def reportSightingPageView(request) :
    return render(request, 'squatchersapp/reportsighting.html')

def contactPageView(request) :
    return render(request, 'squatchersapp/contact.html')


