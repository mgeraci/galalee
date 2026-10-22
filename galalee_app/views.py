from django.shortcuts import render

from .models import Show

def index(request):
    shows = Show.objects.order_by("-date")
    context = {"shows": shows}

    return render(request, "galalee_app/index.html", context)
