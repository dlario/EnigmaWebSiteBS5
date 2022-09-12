from django.shortcuts import render


# Create your views here.
def blog(request):
    return render(request, 'aboutus/blog.html')


def contact(request):
    return render(request, 'aboutus/contact.html')


def team(request):
    return render(request, 'aboutus/team.html')


def home(request):
    return render(request, 'aboutus/home.html')


def engineering(request):
    return render(request, 'aboutus/engineering.html')


def equipmentinspection(request):
    return render(request, 'aboutus/equipmentinspection.html')


def fabrication(request):
    return render(request, 'aboutus/fabrication.html')


def testing(request):
    return render(request, 'aboutus/testing.html')
