from django.urls import path
from .views import aboutPageView, contactPageView, indexPageView, reportSightingPageView, sightingDetailsPageView, sightingsPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("sightings/", sightingsPageView, name="sightings"),   
    path("about/", aboutPageView, name="about"),   
    path("sightingdetails/", sightingDetailsPageView, name="sighting details"),   
    path("report/", reportSightingPageView, name="report sighting"),   
    path("contact/", contactPageView, name="contact")
] 

# DEFINED DJANGO FORMS FOR THIS PROJECT
# Form to create (Report) a new sighting
# Form to lookup a sighting by reporter, location, date, etc.
# Form to update/revise that sighting
# Form to delete a sighting