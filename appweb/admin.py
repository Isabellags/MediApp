from django.contrib import admin
from .models import *

#class ContactoAdmin(admin.ModelAdmin):
    

admin.site.register(Cargo)
admin.site.register(Profesional)
admin.site.register(Contacto)
