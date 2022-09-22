from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Perfil)
admin.site.register(Modulo)
admin.site.register(Permiso)
admin.site.register(Comision)
#admin.site.unregister(Permiso)