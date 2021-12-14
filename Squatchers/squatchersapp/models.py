from django.db import models
from datetime import datetime, timedelta

from django.db.models.fields import TextField

class Reporter(models.Model):
    rep_first = models.CharField(max_length=20)
    rep_last = models.CharField(max_length=20)
    rep_email = models.EmailField(max_length=100)
    rep_birth_date = models.DateField(default=datetime.today)
    rep_believer = models.BooleanField(default=True)


    def __str__(self):
        return ('Reporter Name: ' + self.rep_first + " " + self.rep_last) 

    def save(self):
        self.rep_first = self.rep_first.upper()
        self.rep_last = self.rep_last.upper()
        super(Reporter, self).save()

class Sighting(models.Model):
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    sight_title = models.CharField(max_length=100, blank=True)
    sight_latitude = models.DecimalField(max_digits = 10, decimal_places = 7)
    sight_longitude = models.DecimalField(max_digits = 10, decimal_places = 7)
    sight_date = models.DateField(default='2000-01-01')
    sight_time = models.TimeField(default='00:00:00')
    time_zone = models.CharField(max_length=4, blank=True)
    Country = models.CharField(max_length=50)
    State = models.CharField(max_length=2)
    Image = models.ImageField(upload_to='photos', blank=True)
    Description = TextField(max_length=5000)
    
    def __str__(self):
        return (self.sight_title) 

    def save(self):
        self.Country = self.Country.upper()
        self.State = self.State.upper()
        self.time_zone = self.time_zone.upper()
        super(Sighting, self).save()
        



        