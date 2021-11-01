from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Home page')

def sightingsPageView(request) :
    return HttpResponse('sightings database goes here')

def aboutPageView(request) :
    return HttpResponse('about us goes here')

def sightingDetailsPageView(request, sighting_id) :
    return HttpResponse('sighting details for sighting ' + str(sighting_id) + ' go here')

def reportSightingPageView(request) :
    return HttpResponse('This is where you can report a sighting')
