from django.contrib import admin
from .models import Visitor, Convener, Meeting
# Register your models here.

admin.site.register(Visitor)
admin.site.register(Convener)
admin.site.register(Meeting)

