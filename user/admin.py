from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'slug', 'id')
    list_display_links = ('owner', 'name')
    list_filter = ('owner',)
    search_fields = ('name',)
    readonly_fields = ('id', 'slug')
# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Hesap)