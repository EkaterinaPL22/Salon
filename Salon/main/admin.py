from django.contrib import admin
from .models import Procedure, Client, Order


admin.site.register(Procedure)

admin.site.register(Client)

admin.site.register(Order)
# Register your models here.
