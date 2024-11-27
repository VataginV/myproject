from django.db import models
from filer.fields.image import FilerImageField
from PIL import Image
import os

class SliderImage(models.Model):
    title = models.CharField(max_length=255)
    image = FilerImageField(on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    def get_thumbnail(self):
        img = Image.open(self.image.path) 
        img.thumbnail((150, 150))
        thumbnail_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'thumbnail.jpg')
        img.save(thumbnail_path)

        return thumbnail_path

    class Meta:
        ordering = ['order']
