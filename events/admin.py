from django.contrib import admin

# Register your models here.
from .models import Event

class EventAdmin(admin.ModelAdmin):
    # def time_seconds(self, obj):
    #     return obj.logdate.strftime("%d %b %Y %I:%M:%S")
    # time_seconds.admin_order_field = 'datetimefield'
    # time_seconds.short_description = 'Precise Time' 
    list_display = ["name", "logdate", "address", "created_date"]
    
   

admin.site.register(Event, EventAdmin)