from django.db import models
from medical_records.models import MedicalRecords
from account.models import Profile


class Treatments(models.Model):
    medical_record = models.ForeignKey(MedicalRecords,on_delete=models.CASCADE,related_name='treatment_records')
    start_date = models.DateField()
    end_date = models.DateField()
    method = models.TextField(verbose_name='Метод лечения (например, "операция", "медикаментозная терапия")')
    medication = models.TextField(verbose_name='Название препарата')
    dosage = models.TextField(verbose_name='Дозировка')
    notes = models.TextField()


class TreatmentsSchedule(models.Model):
    treatment = models.ForeignKey(Treatments,on_delete=models.CASCADE,related_name='treatment_schedule')
    scheduled_time = models.DateTimeField()
    action_type = models.CharField(max_length=20,verbose_name='Тип действия')
    nurse = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,limit_choices_to={'role__startswith':'nurse'},related_name='treatment_schedule',verbose_name='Медсестра')
    