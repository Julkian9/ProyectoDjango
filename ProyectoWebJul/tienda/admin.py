from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class productoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(CategoriaProd, categoriaAdmin)
admin.site.register(Producto, productoAdmin)