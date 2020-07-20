from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo
import random


def index(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PhotoForm()
    return render(request, 'mixer/add.html', {'form': form})


def mix(request):
    print(request.POST.get('fst_image'))
    length = Photo.objects.count()
    fst = Photo.objects.get(id=random.randint(1, length))
    scd = Photo.objects.get(id=random.randint(1, length))
    while scd == fst:
        scd = Photo.objects.get(id=random.randint(1, length))
    context = {
        'fst': fst,
        'scd': scd
    }
    return render(request, 'mixer/mixer.html', context)
