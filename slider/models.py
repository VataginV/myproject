from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from filer.fields.image import FilerImageField
from django.db import models

class SliderImage(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = FilerImageField(verbose_name="Изображение", on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ['order']
        verbose_name = "Слайдерное изображение"
        verbose_name_plural = "Слайдерные изображения"

    def __str__(self):
        return self.title