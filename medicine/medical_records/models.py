from django.db import models
from medic.models import Hospitalizations
from account.models import Profile
from patients.models import Patients


class MedicalRecords(models.Model):
    hospitalizations = models.ForeignKey(Hospitalizations,on_delete=models.CASCADE,related_name='medical_records')
    notes_for_doctor = models.TextField(verbose_name='Запись для врачей')
    notes_for_nurses = models.TextField(verbose_name='Запись для медсестер')
    doctor = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,limit_choices_to={'role__startswith':'doctor'},related_name='medical_record_doc',verbose_name='Лечащий врач')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.doctor} - {self.hospitalizations}'
    
class MedicalRecordsPatient(models.Model):
    patient = models.ForeignKey(Patients,on_delete=models.CASCADE,related_name='medical_record_of_patient')
    blood_type = models.IntegerField(verbose_name='Тип крови')
    rh_factor = models.CharField(max_length=25,verbose_name='Резус фактор пациента')
    chronic_diseases = models.TextField(verbose_name='Хронические болезни пациента')
    allergies = models.TextField(verbose_name='Аллергии')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient}'