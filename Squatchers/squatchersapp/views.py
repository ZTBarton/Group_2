from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'squatchersapp/index.html')

def sightingsPageView(request) :
    return render(request, 'squatchersapp/sightings.html')

def aboutPageView(request) :
    return render(request, 'squatchersapp/about.html')

# this doesn't work right now
def sightingDetailsPageView(request) :
    return render(request, 'squatchersapp/sightingdetails.html')

def reportSightingPageView(request) :
    return render(request, 'squatchersapp/reportsighting.html')

def contactPageView(request) :
    return render(request, 'squatchersapp/contact.html')


