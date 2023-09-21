from django.contrib import admin

from .models import Asana


@admin.register(Asana)
class AsanaAdmin(admin.ModelAdmin):
    pass
