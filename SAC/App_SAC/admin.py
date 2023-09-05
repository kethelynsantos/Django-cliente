from django.contrib import admin


# Register your models here.
from .models import Cliente, Atendente
admin.site.register(Cliente)


admin.site.register(Atendente)


