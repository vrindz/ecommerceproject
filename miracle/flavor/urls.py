from django.urls import path
from . import views

urlpatterns = [


    path('', views.index,name='base'),
    path('about/', views.about,name='about'),
    path('product/',views.product,name='product'),
    path('recipes/',views.recipes,name='recipes'),
    path('contact/',views.contact,name='contact'),
    path('privacy/',views.privacy,name='privacy')
    ]