from django.contrib import admin

# Register your models here.
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "logdate", "address"]
    def time_seconds(self, obj):
        return obj.datetimefield.strftime("%d %b %Y %h:%M:%S")
    time_seconds.admin_order_field = 'datetimefield'
    time_seconds.short_description = 'Precise Time' 
   

admin.site.register(Event, EventAdmin)