from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def fintech(request):
    return render(request, 'fintech.html')


def edtech(request):
    return render(request, 'edtech.html')


def health(request):
    return render(request, 'health.html')


def insurance(request):
    return render(request, 'insurance.html')


def constraction(request):
    return render(request, 'constraction.html')