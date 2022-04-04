from django.shortcuts import render,redirect
#from django.contrib.auth.models import User, auth
#from django.contrib import messages
from.models import contact
#from django.http import HttpResponse
#from contact.models import contact

def saveEnquiry(request):
    if request.method == 'POST' :
        name = request.POST['name']
        phone_no = request.POST['phone_no']
        email_ID = request.POST['email_ID']
        message = request.POST['message']
        en=contact(name=name,phone_no=phone_no,email_ID=email_ID,message=message)
        en.save()
        return redirect('/')

