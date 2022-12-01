import email
from django.db import models
from django.db.models.fields import DateTimeField
from django_countries.fields import CountryField

# Create your models here.


class DayAction(models.Model):
    day_name = models.CharField(max_length=255, null=True, blank=True)
    day_title = models.CharField(max_length=255, null=True, blank=True)
    place_name = models.CharField(max_length=255, null=True, blank=True)
    day_desc = models.TextField(null=True, blank=True)
    day_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.day_title

class TourPackage(models.Model):
    package_name = models.CharField(max_length=255, null=True, blank=True)
    package_desc = models.TextField(null=True, blank=True)
    package_slogan = models.CharField(max_length=255, null=True, blank=True)
    main_place = models.CharField(max_length=255, null=True, blank=True)
    days_to_travel = models.IntegerField(null=True, blank=True)
    ratings = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    packagePrice = models.DecimalField(max_digits=8, decimal_places=2)
    packageImage = models.ImageField(null=True, blank=True)
    day_actions = models.ManyToManyField(DayAction, related_name='day_actions', blank=True)
    country = CountryField(null=True, blank=True,blank_label='(select country)')

    def __str__(self):
        return self.package_name

class Slider(models.Model):
    slide_title = models.CharField(max_length=255, null=True, blank=True)
    slide_image = models.ImageField(null=True, blank=True)
    slide_descr = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.slide_title

class Service(models.Model):
    service_name = models.CharField(max_length=255, null=True, blank=True)
    service_class_name = models.CharField(max_length=255, null=True, blank=True, default='bx bxl-dribbble')
    sevice_desc = models.TextField(null=True, blank=True)
    serviceImage = models.ImageField(null=True, blank=True)
    date_added = DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.service_name

class Message(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date_added = DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    hotelImage = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.name


class Destination(models.Model):
    location = models.CharField(max_length=255, null=True, blank=True)
    destinationImage = models.ImageField(null=True, blank=True)
    slogan = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.location

class contactUs(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name