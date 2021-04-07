from django.contrib import admin

# Register your models here.
from .models import Contact,Index


admin.site.register(Contact)
admin.site.register(Index)