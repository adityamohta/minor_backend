from django.contrib import admin
from .models import Device, Tracking


class TrackingInLine(admin.TabularInline):
    model = Tracking
    extra = 1


class DeviceModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        '__str__',
        'number',
        'network_operator',
        'active',
        'created_at',
        'updated_at'
    ]
    list_display_links = ['id', '__str__']
    raw_id_fields = ['user']
    inlines = [TrackingInLine]

    class Meta:
        model = Device


class TrackingModelAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        '__str__',
        'latitude',
        'longitude',
        'capture_time',
        'created_at',
        'updated_at',
    ]
    list_display_links = ['id', '__str__']
    raw_id_fields = ['device']

    class Meta:
        model = Tracking


admin.site.register(Device, DeviceModelAdmin)
admin.site.register(Tracking, TrackingModelAdmin)
