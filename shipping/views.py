from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'admin/home.html')
    
def about(request):
    return render(request,'admin/about.html') 
       
def contact(request):
    return render(request,'admin/contact.html')

def feature(request):
    return render(request,'admin/feature.html')

def price(request):
    return render(request,'admin/price.html')

def quote(request):
    return render(request,'admin/quote.html') 

def service(request):
    return render(request,'admin/service.html') 

def team(request):
    return render(request,'admin/team.html') 

def testimonial(request):
    return render(request,'admin/testimonial.html')

def notfound(request):
    return render(request,'admin/404.html') 
