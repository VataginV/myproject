from django.db import models
from filer.fields.image import FilerImageField
from PIL import Image

class SliderImage(models.Model):
    title = models.CharField(max_length=255)
    image = FilerImageField(on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    def get_thumbnail(self):
        img = Image.open(self.image)
        img.thumbnail((150, 150))
        img.save('path/to/save/thumbnail.jpg') 
        return 'path/to/save/thumbnail.jpg'
    class Meta:
        ordering = ['order']
        
    