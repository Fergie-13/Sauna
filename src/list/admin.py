from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Besedka)
admin.site.register(models.Billiard)
admin.site.register(models.Pool)