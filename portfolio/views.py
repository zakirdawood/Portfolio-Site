from django.shortcuts import render
from django.core.mail import send_mail
import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def check(email):   
  
    if(re.search(regex,email)):   
        return True   
    else:   
        return False 

# Create your views here.
def index(request):
    return render(request, 'portfolio/home.html')

def index2(request):
    return render(request, 'portfolio/skills.html')

def index3(request):
    return render(request, 'portfolio/projects.html')

def index4(request):
    return render(request, 'portfolio/gallery.html')

def index5(request):
    return render(request, 'portfolio/contact.html')

def contact(request):
    message_name = request.POST.get("message-name")
    message_subject = request.POST.get("message-subject")
    message_email = request.POST.get("message-email")
    premessage = str(request.POST.get("message"))
    message = "From: " + str(message_name) + "\n\n" + "Contact: " + message_email + "\n\n"  + "Message: " + premessage

    if str(message_name) == "" or message_name == None:
        return render(request, 'portfolio/errorsent.html')

    if check(str(message_email)) == False:
        return render(request, 'portfolio/errorsent.html')

    if str(message_subject) == "" or message_subject == None:
        return render(request, 'portfolio/errorsent.html')

    if premessage == "" or premessage == None:
        return render(request, 'portfolio/errorsent.html')


    send_mail(
        message_subject, #subject
        message, #message
        message_email, #from
        [''], #to email
        fail_silently=False
    )

    return render(request, 'portfolio/sentpage.html')