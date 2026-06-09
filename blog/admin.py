from django.contrib import admin
from . import models

@admin.register(models.Fighter)
class FighterAdmin(admin.ModelAdmin):
    exclude = ('views',)




admin.site.register(models.FactsMk)