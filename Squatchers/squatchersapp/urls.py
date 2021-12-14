from django.urls import path
from .views import aboutPageView, contactPageView, indexPageView, reportSightingPageView, sightingDetailsPageView, sightingsPageView, editSightingPageView, DeleteSightingPageView, updateSighting, createSighting

urlpatterns = [
    path("", indexPageView, name="index"),
    path("sightings/", sightingsPageView, name="sightings"),   
    path("about/", aboutPageView, name="about"),   
    path("sightingdetails/", sightingDetailsPageView, name="sighting details"),   
    path("report/", reportSightingPageView, name="report sighting"),   
    path("contact/", contactPageView, name="contact"),
    path("edit/<int:id>", editSightingPageView, name="edit"),
    path("delete/<int:id>", DeleteSightingPageView, name="delete"),
    path("update/", updateSighting, name="update"),
    path("create/", createSighting, name="create")
] 

# DEFINED DJANGO FORMS FOR THIS PROJECT
# Form to create (Report) a new sighting
# Form to lookup a sighting by reporter, location, date, etc.
# Form to update/revise that sighting
# Form to delete a sighting