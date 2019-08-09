from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import mainApplication
# Create your views here.


def mainPage(request):
    return render(request, 'mainPage.html')

def mainApplicant(request):
    return render(request, 'mainApplicant.html')

def createMain(request):
    app = mainApplication()
    app.title = request.POST['title']
    app.pub_date = timezone.datetime.now()
    app.body = request.POST['body']
    app.author = request.user
    app.save()
    return redirect('/')   