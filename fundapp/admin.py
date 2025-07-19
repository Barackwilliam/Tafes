from django.contrib import admin
from .models import Contribution

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'timestamp')
    search_fields = ('name',)
