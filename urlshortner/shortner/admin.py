from django.contrib import admin
from .models import Url


class UrlDisplay(admin.ModelAdmin):
    list_display = ('link','uuid')


admin.site.register(Url,UrlDisplay)