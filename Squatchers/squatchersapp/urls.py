from django.urls import path
from .views import aboutPageView, indexPageView, reportSightingPageView, sightingDetailsPageView, sightingsPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("sightings/", sightingsPageView, name="sightings"),   
    path("about/", aboutPageView, name="about"),   
    path("sightingdetails/<int:sighting_id>", sightingDetailsPageView, name="sighting details"),   
    path("report/", reportSightingPageView, name="report sighting")   
] 