from django.contrib import admin
from .models import category,films

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","img")



admin.site.register(category , CategoryAdmin)
admin.site.register(films)