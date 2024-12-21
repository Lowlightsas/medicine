from django.contrib import admin
from .models import Hospitalizations

@admin.register(Hospitalizations)
class HospitalizationsAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('patient', 'admession_date', 'department', 'assigned_doctor', 'discharge_date', 'created', 'updated')
    
    # Add filters for easier navigation
    list_filter = ('department', 'assigned_doctor', 'admession_date', 'discharge_date')
    
    # Enable search functionality
    search_fields = ('patient__name', 'reason_for_admission', 'assigned_doctor__username')
    
    # Order the records
    ordering = ('-admession_date',)
    
    # Read-only fields (if required)
    readonly_fields = ('created', 'updated')

    # Group fields into sections
    fieldsets = (
        ('Patient Details', {
            'fields': ('patient', 'reason_for_admission', 'department')
        }),
        ('Doctor and Dates', {
            'fields': ('assigned_doctor', 'admession_date', 'discharge_date')
        }),
        ('Metadata', {
            'fields': ('created', 'updated')
        }),
    )
