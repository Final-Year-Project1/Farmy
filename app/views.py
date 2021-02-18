from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student
from django.contrib import messages

from app.forms import studentForm

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

def registration(request):
    return render(request,'registrationform.html')

def showStudents(request):
    if (request.method=='POST'):
        
        form = studentForm(request.POST,request.FILES) 

        if( form.is_valid() ):
            print("\nvalid\n")
            roll = request.POST['roll']
            imgname = form.cleaned_data
            form.save()
            
            
        else:
            # form is not valid i.e. if invalid values are given

            pass
        
        
        messages.info(request,'Successfully Registered')

        return redirect('/')

    else:    
        
        data = student.objects.all()

        return render(request,'showStudents.html',{'data':data})
    