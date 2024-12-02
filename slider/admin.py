from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderImage  

class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_editable = ('image',)

admin.site.register(SliderImage, SliderImageAdmin)
