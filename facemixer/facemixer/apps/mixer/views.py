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
    if request.POST:
        winner_id, loser_id = list(request.POST.keys())[1].split('?')
        winner = Photo.objects.get(id=winner_id)
        loser = Photo.objects.get(id=loser_id)
        EA = 1 / (1 + 10 ** ((loser.photo_rating - winner.photo_rating) / 400))
        EB = 1 / (1 + 10 ** ((winner.photo_rating - loser.photo_rating) / 400))
        RA = winner.photo_rating + 20 * (1 - EA)
        RB = loser.photo_rating + 20 * (0 - EB)
        winner.photo_rating = RA
        loser.photo_rating = RB
        winner.save()
        loser.save()
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
