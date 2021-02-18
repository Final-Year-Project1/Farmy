# forms.py 
from django import forms 
from .models import *
  
class studentForm(forms.ModelForm): 
    class Meta: 
        model = student 
        fields = ['profile_image','roll','name','per'] 