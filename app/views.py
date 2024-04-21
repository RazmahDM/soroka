from django.shortcuts import render
from django.http import HttpResponse
from app.models import PortfolioItem, ServiceItem


# Create your views here.
def index(request):



    return render(request, "index.html")
 
def services(request):

    services = ServiceItem.objects.filter()

    data = {"services": services}

    return render(request, "services.html", context=data)

def portfolio(request):

    portfolio = PortfolioItem.objects.all()

    data = {"portfolio": portfolio}

    return render(request, "portfolio.html", context=data)
 
def contact(request):
    return render(request, "contact.html")