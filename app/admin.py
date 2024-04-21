from django.contrib import admin
from app.models import PortfolioItem, ServiceItem

# Register your models here.


class PortfolioItemAdmin(admin.ModelAdmin):
    pass


class ServiceItemItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(ServiceItem, ServiceItemItemAdmin)