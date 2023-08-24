# Create your views here.
from django.shortcuts import render


def chooser(request):
    return render(request, 'chooser.html')
