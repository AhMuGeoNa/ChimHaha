from django.shortcuts import render
from datetime import datetime

def experiment(request):

    return render(request, 'experiment.html', context = {})