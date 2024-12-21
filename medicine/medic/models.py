from django.db import models 
from patients.models import Patients
from account.models import Profile

class Hospitalizations(models.Model):
    patient = models.ForeignKey(Patients,on_delete=models.CASCADE,related_name='hospitalizations_patients')
    admession_date = models.DateField(verbose_name='Дата поступления')
    department = models.CharField(max_length=50,choices=Patients.DEPARTMENT_CHOICES,verbose_name='Отделение')
    reason_for_admission = models.TextField(verbose_name='Причина поступления')
    assigned_doctor = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,limit_choices_to={'role__startswith':'doctor'},related_name='hospitalizations_doctor',verbose_name='Лечащий врач')
    discharge_date = models.DateField(verbose_name='Дата выписки')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.patient} - {self.department} {self.admession_date}'
    