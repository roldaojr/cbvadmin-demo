from __future__ import unicode_literals, absolute_import
import cbvadmin
from .models import Category, Computer


@cbvadmin.register(Category)
class CategoryAdmin(cbvadmin.options.ModelAdmin):
    list_display = ('name',)


@cbvadmin.register(Computer)
class ComputerAdmin(cbvadmin.options.ModelAdmin):
    list_display = ('name', 'category', 'active')
    filter_fields = ('name', 'active')
