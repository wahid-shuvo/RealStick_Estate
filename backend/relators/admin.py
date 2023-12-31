from django.contrib import admin

from django.contrib import admin
from .models import Relator


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date_hired')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Relator, RealtorAdmin)
