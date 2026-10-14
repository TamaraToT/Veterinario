from django.contrib import admin
from cliente.models import Cliente
from cliente.models import Mascota
from cliente.models import Atencion

admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Atencion)
