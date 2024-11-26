from django.shortcuts import render
from .models import SliderImage

# Create your views here.
def gl(request):
    slider_images = SliderImage.objects.all() 
    context = {
        'slider_images': slider_images
    }
    return render(request, "index.html", context)