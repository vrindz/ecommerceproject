from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def index(request):
    # return HttpResponse("Home Page")
    return render(request, "index.html")

def base(request):
    #return HttpResponse("Home Page")
    return render(request, "base.html")
def about(request):

    #return HttpResponse("About Page")


    return render(request, "about.html")
def product(request):

    #return HttpResponse("About Page")


    return render(request, "product.html")
def recipes(request):

    #return HttpResponse("About Page")


    return render(request, "recipes.html")
def contact(request):

    #return HttpResponse("About Page")


    return render(request, "contact.html")
def privacy(request):

    #return HttpResponse("About Page")


    return render(request, "privacy.html")






