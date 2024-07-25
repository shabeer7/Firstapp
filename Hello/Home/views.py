from django.shortcuts import render,HttpResponse
from Home.models import contact

# Create your views here.

def home(request):
    # return HttpResponse("Hi you are in Home page")
    context = {
        "name" : "shabeer",
        "age"  : 24
    }
    return render (request,"index.html", context )
def about(request):
    return render(request, "about.html")
    # return HttpResponse("Hi you are in About page")
def services(request):
    return render(request, "services.html")
    # return HttpResponse("Hi you are in Services page")
def contact(request):

    if request == "POST":
        Name=request.POST.get("Name")
        Number=request.POST.get("Number")
        Email=request.POST.get("Email")
        Password=request.POST.get("Password")
        contact=contact(Name='Name', Number='Number', Email='Email', Password='Password' )
        contact.save()

    return render(request, "contact.html")
    # return HttpResponse("Hi you are in Contact page")