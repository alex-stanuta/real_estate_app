from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'is_mvp', 'email', 'hire_date')
	list_display_links = ('id', 'name')

admin.site.register(Realtor, RealtorAdmin)
