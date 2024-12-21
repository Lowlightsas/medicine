from django.contrib import admin
from .models import Treatments, TreatmentsSchedule


@admin.register(Treatments)
class TreatmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'medical_record', 'method', 'start_date', 'end_date', 'medication')
    list_filter = ('start_date', 'end_date', 'method')
    search_fields = ('medical_record__id', 'method', 'medication')
    ordering = ('-start_date',)


@admin.register(TreatmentsSchedule)
class TreatmentsScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'treatment', 'scheduled_time', 'action_type', 'nurse')
    list_filter = ('action_type', 'scheduled_time', 'nurse')
    search_fields = ('treatment__method', 'action_type', 'nurse__user__username')
    ordering = ('-scheduled_time',)
