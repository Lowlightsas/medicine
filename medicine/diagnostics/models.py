from django.db import models
from patients.models import Patients
from medical_records.models import MedicalRecords

class Diagnostics(models.Model):
    patient = models.ForeignKey(Patients,on_delete=models.CASCADE,related_name='diagnostics_patients')
    medical_records = models.ForeignKey(MedicalRecords,on_delete=models.CASCADE,related_name='diagnostics_records')
    type = models.CharField(max_length=100,verbose_name='тип анализа')
    date = models.DateField(verbose_name='Дата анализа')
    result = models.FileField(
        upload_to='diagnostics_results/',  
        verbose_name='Результат анализа'
    )
    def __str__(self):
        return f'{self.type} ({self.date}) - {self.patient}'