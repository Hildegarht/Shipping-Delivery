from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home.html',views.home, name='home'),
    path('about.html',views.about, name='about'),
    path('contact.html',views.contact, name='contact'),
    path('feature.html',views.feature, name='feature'),
    path('price.html',views.price, name='price'),
    path('quote.html',views.quote, name='quote'),
    path('service.html',views.service, name='service'),
    path('team.html',views.team, name='team'),
    path('testimonial.html',views.testimonial, name='testimonial'),
    path('notfound.html',views.notfound, name='404'),
]