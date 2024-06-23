from django.contrib import admin
from apps.utils.models import (
    State,
    District,
    Z2HSettings
)

# Register your models here.

class StateAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'is_active')
    search_fields = ('name',)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'state', 'is_active')
    list_filter = ('state',)
    search_fields = ('name',)

class Z2HSettingsAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'description', 'value', 'is_active')

admin.site.register(State, StateAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Z2HSettings, Z2HSettingsAdmin)