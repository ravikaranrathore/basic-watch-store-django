from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'variable' : "SnorLax 2OP",
        'var2' : "LODA LELEOOOOO "
    }
    messages.success(request, 'This is a test message')
    return render(request, 'index.html', context)
    #return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')
 #   return HttpResponse("This is about page")

def ser(request):
    return render(request, 'services.html')
#    return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mob = request.POST.get('mob')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact = Contact(name=name, email=email, mob = mob, desc = desc, date = date)
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")
