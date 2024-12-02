from django.shortcuts import render
from .models import SliderImage
from django.conf import settings

def gl(request):
    slider_images = SliderImage.objects.all() 
    context = {
        'slider_images': slider_images,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, "index.html", context)