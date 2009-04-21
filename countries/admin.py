from django.contrib import admin
from countries.models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('printable_name', 'name', 'iso', 'iso3', 'numcode')
    ordering = ('printable_name',)
    search_fields = ('printable_name', 'name')

admin.site.register(Country, CountryAdmin)

