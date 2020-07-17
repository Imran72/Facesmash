from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, somebody. It's Imran. Wherever I am")
