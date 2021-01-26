from django.shortcuts import render
from contactus.forms import contactforemail
from django.core.mail import send_mail
from django.contrib import messages

def contactsendmail(request):
    if request.method=='GET':
        form=contactforemail()
    else:
        form=contactforemail(request.POST)
        if form.is_valid():
            frommail=form.cleaned_data['fromemail']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            send_mail(subject,message,frommail,['kartikkhanna93@gmail.com',frommail])
            messages.success(request, "Your message has been sent")
        else:
            messages.success(request, "Your message has been not been sent") #value in inverted commas is name field in form

    
    return render(request,'contact-page.html',{'form':form})
