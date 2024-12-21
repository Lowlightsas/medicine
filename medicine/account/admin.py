from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','role','department','contact_number','email']
    list_filter = ['role','department']
    search_fields = ('user__username','contact_number','email')
    ordering = ('role','department')
    fieldsets = (
        (None, {
            'fields':('user','photo','date_of_birth','contact_number','email')

        }),
        ('Role and Department',{
            'fields':('role','department')
        })
    )