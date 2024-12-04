from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderImage  


class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'image')
    list_editable = ('order',)
    prepopulated_fields = {'title': ('image',)}
    
admin.site.register(SliderImage, SliderImageAdmin)
