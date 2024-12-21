from django.contrib import admin
from .models import MedicalRecords, MedicalRecordsPatient

@admin.register(MedicalRecords)
class MedicalRecordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'hospitalizations', 'created', 'updated')
    list_filter = ('doctor', 'created', 'updated')  
    search_fields = ('doctor__user__username', 'hospitalizations__id') 
    ordering = ('-created',)  
    readonly_fields = ('created', 'updated')  
    fieldsets = (
        (None, {
            'fields': ('hospitalizations', 'doctor', 'notes_for_doctor', 'notes_for_nurses')
        }),
        ('Дополнительная информация', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',),  
        }),
    )

@admin.register(MedicalRecordsPatient)
class MedicalRecordsPatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'blood_type', 'rh_factor', 'created', 'updated')
    list_filter = ('blood_type', 'rh_factor', 'created', 'updated')  
    search_fields = ('patient__name', 'chronic_diseases', 'allergies')  
    ordering = ('-created',) 
    readonly_fields = ('created', 'updated') 
    fieldsets = (
        (None, {
            'fields': ('patient', 'blood_type', 'rh_factor', 'chronic_diseases', 'allergies')
        }),
        ('Дополнительная информация', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',),
        }),
    )
