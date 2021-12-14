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
    date = data.sight_date.strftime('%Y-%m-%d')
    time = data.sight_time.strftime('%H:%M:%S')
    context = {
        'sighting' : data,
        'date' : date,
        'time' : time
    }
    return render(request, 'squatchersapp/editSighting.html', context)

def updateSighting(request):
    if request.method == 'POST':
        sightingid = request.POST['id']

        record = Sighting.objects.get(id=sightingid)

        record.sight_title = request.POST['title']
        record.sight_latitude = request.POST['latitude']
        record.sight_longitude = request.POST['longitude']
        record.Description = request.POST['description']
        record.sight_date = request.POST['date']
        record.sight_time = request.POST['time']
        record.time_zone = request.POST['timezone']
        record.Country = request.POST['country']
        record.State = request.POST['state']

        record.save()

    return sightingsPageView(request)

def DeleteSightingPageView(request, id):
    data = Sighting.objects.get(id=id)
    data.delete()
    return sightingsPageView(request)

def aboutPageView(request) :
    return render(request, 'squatchersapp/about.html')

def sightingDetailsPageView(request) :
    return render(request, 'squatchersapp/sightingdetails.html')

def reportSightingPageView(request) :
    data = Reporter.objects.all()

    context = {
        'reporters' : data
    }
    return render(request, 'squatchersapp/reportSighting.html', context)

def contactPageView(request) :
    return render(request, 'squatchersapp/contact.html')

def createSighting(request):
    if request.method == 'POST':
        record = Sighting()

        record.sight_title = request.POST['title']
        record.sight_latitude = request.POST['latitude']
        record.sight_longitude = request.POST['longitude']
        record.Description = request.POST['description']
        record.sight_date = request.POST['date']
        record.reporter_id = request.POST['reporterid']
        record.sight_time = request.POST['time']
        record.time_zone = request.POST['timezone']
        record.Country = request.POST['country']
        record.State = request.POST['state']

        record.save()
    return sightingsPageView(request)


