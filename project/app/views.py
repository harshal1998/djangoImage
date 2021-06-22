from django.http import request
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def a(request):
    if request.method == 'POST':
        form = hotelform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/display")

    else:
        form = hotelform()
    return render(request, 'home.html', {'form': form})


def b(request):
    data = hotel.objects.all()
    return render(request, 'display.html', {'data': data})
