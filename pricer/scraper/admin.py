from django.contrib import admin

from .models import Product, Link, Price


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Product, BaseAdmin)
admin.site.register(Link, BaseAdmin)
admin.site.register(Price, BaseAdmin)
