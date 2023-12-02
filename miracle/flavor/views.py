from django.shortcuts import render
from .models import Product
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

    dict_prod = {
        'product': Product.objects.all()
      }
    return render(request, "product.html",dict_prod)

def recipes(request):

    #return HttpResponse("About Page")


    return render(request, "recipes.html")
def contact(request):

    #return HttpResponse("About Page")


    return render(request, "contact.html")
def privacy(request):

    #return HttpResponse("About Page")


    return render(request, "privacy.html")






