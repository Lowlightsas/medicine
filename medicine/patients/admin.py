from django.contrib import admin
from .models import Patients

@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'middle_name', 'department', 'region', 'gender', 'iin', 'contact_number', 'created', 'updated')
    list_filter = ('gender', 'region', 'department', 'created', 'updated')  
    search_fields = ('last_name', 'first_name', 'middle_name', 'iin', 'contact_number')  
    ordering = ('-created',) 
    readonly_fields = ('created', 'updated')  
    fieldsets = (
        ('Личная информация', {
            'fields': ('first_name', 'last_name', 'middle_name', 'date_of_birth', 'gender', 'iin', 'contact_number', 'address', 'region'),
        }),
        ('Информация о госпитализации', {
            'fields': ('department',),
        }),
        ('Служебная информация', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',),  
        }),
    )
