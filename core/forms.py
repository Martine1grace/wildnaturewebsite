from django import forms
from django.db.models.fields import TextField
from django.forms import ModelForm, fields
from core.models import TourPackage, Service, DayAction
from django.forms import Select, TextInput, Textarea, FileField, NumberInput, ImageField


class TourPackageForm(forms.ModelForm):
    class Meta:
        model = TourPackage
        fields = '__all__'
        widgets = {
            'package_name': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter package name"}),
            'package_slogan': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter package description"}),
            'main_place': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter main place"}),
            'days_to_travel': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter days to travel"}),
            'ratings': NumberInput(attrs={'class': 'form-control', 'placeholder': "0.00"}),
            'packagePrice': NumberInput(attrs={'class': 'form-control', 'placeholder': "0.00"}),        
            'package_desc': Textarea(attrs={'class': 'form-control'})
        }
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'service_name': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter service name"}),
            'service_class_name': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter service class name"}),     
            'sevice_desc': Textarea(attrs={'class': 'form-control'})
        }
        
class DayActionForm(forms.ModelForm):
    class Meta:
        model = DayAction
        fields = '__all__'
        widgets = {
            'day_name': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter day name"}),
            'day_title': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter day title"}),
            'place_name': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter service class name"}),     
            'day_desc': Textarea(attrs={'class': 'form-control'})
        }

#class sliderForm(forms.ModelForm):
 #   class Meta:
  #      model = slider
   #     fields = '__all__'
    #    widgets = {
     #       'slide_title': TextInput(attrs={'class': 'form-control', 'placeholder': "Enter slider title"}),
      #      'slide_desc': Textarea(attrs={'class': 'form-control'})
       # }