from django.http import HttpResponse

from .models import Show

def index(request):
    shows = Show.objects.order_by("-date")
    output = ", ".join([show.venue for show in shows])
    return HttpResponse(output)
