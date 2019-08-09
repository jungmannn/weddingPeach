from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import dressApplicant

# Create your views here.
def kindAnimal(request):
    return render(request, 'kindAnimal.html')

def dressApplication(request):
    return render(request, 'dressApplicant.html')

def createDress(request):
    app = dressApplicant()
    app.title = request.POST['title']
    app.pub_date = timezone.datetime.now()
    app.body = request.POST['body']
    app.author = request.user
    app.save()
    return redirect('/')   