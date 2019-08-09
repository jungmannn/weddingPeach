from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Application

# Create your views here.
def application(request):
    return render(request, 'application.html')

def createApplication(request):
    app = Application()
    app.title = request.POST['title']
    app.pub_date = timezone.datetime.now()
    app.body = request.POST['body']
    app.author = request.user
    app.save()
    return redirect('/personal')