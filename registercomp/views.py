from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def regicomplaint(request):
    return render(request, 'complaint.html')