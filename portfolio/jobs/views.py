from django.shortcuts import render
from .models import job

def Home(request):
    jobs = job.objects
    return render(request,  'jobs/home.html', {'jobs':jobs} )
