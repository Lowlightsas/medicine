from django.db import models
from django.conf import settings

class Profile(models.Model):
    
    ROLE_CHOICES = [
        ('doctor','Doctor'),
        ('nurse','Nurse'),
    ]
    DEPARTMENT_CHOICES = [
        ('surgery', 'Хирургическое отделение'),
        ('urology', 'Урологическое отделение'),
        ('ent', 'Отоларингологическое отделение'),
        ('maxillofacial', 'Отделение челюстно–лицевой хирургии'),
        ('traumatology', 'Травматологическое отделение'),
        ('neurosurgery', 'Нейрохирургическое отделение'),
        ('ophthalmology', 'Офтальмологическое отделение'),
        ('anesthesia', 'Отделение анестезиологии и реанимации'),
        ('operating_room', 'Операционное отделение'),
        ('angiography', 'Отделение рентген-ангио-хирургических методов диагностики и лечения'),
        ('transfusion', 'Отделение трансфузиологии (переливания крови)'),
        ('maternity', 'Родильное отделение'),
        ('neonatal_reanimation', 'Отделение реанимации новорожденных'),
        ('neonatal_pathology', 'Отделение патологии новорожденных и выхаживания недоношенных'),
        ('cardiology', 'Кардиологическое отделение'),
        ('cardiovascular_surgery', 'Отделение сердечно-сосудистой хирургии'),
        ('neurology', 'Неврологическое отделение с инсультным центром'),
        ('diagnostic_center', 'Клинико-диагностический центр'),
        ('pathology', 'Патологоанатомическое отделение'),
        ('gynecology', 'Гинекологическое отделение'),
        ('rehabilitation', 'Отделение восстановительного лечения и медицинской реабилитации'),
    ]
    SPECIALTIES = [
    # Врачи
    ('cardiologist', 'Врач-кардиолог'),
    ('otolaryngologist', 'Врач-отоларинголог'),
    ('therapist', 'Врач-терапевт'),
    ('hospital_therapist', 'Врач-терапевт госпитального отделения'),
    ('manual_therapy', 'Врач мануальной терапии'),
    ('reflexologist_neurologist', 'Врач-рефлексотерапевт-невролог'),
    ('psychiatrist', 'Врач-психиатр'),
    ('psychiatrist_narcologist', 'Врач-психиатр-нарколог'),
    ('hematologist', 'Врач-гематолог'),
    ('rheumatologist', 'Врач-ревматолог'),
    ('ophthalmologist', 'Врач-офтальмолог'),
    ('urologist', 'Врач-уролог'),
    ('gynecologist', 'Врач-акушер-гинеколог'),
    ('dermatologist', 'Врач-дерматовенеролог'),
    ('diagnostics_doctor', 'Врач функциональной диагностики'),
    ('surgeon', 'Врач-хирург'),
    ('neurosurgeon', 'Врач-нейрохирург'),
    ('traumatologist', 'Врач-травматолог'),
    ('maxillofacial_surgeon', 'Врач-челюстно-лицевой хирург'),
    ('angiographer', 'Врач-ангиографист'),
    ('transfusiologist', 'Врач-трансфузиолог'),
    ('neonatologist', 'Врач-неонатолог'),
    ('cardiovascular_surgeon', 'Врач-сердечно-сосудистый хирург'),
    ('anesthesiologist', 'Врач-анестезиолог'),
    
    # Медицинский персонал
    ('feldsher_commission', 'Фельдшер военно-врачебной комиссии'),
    ('nurse_commission', 'Медицинская сестра военно-врачебной комиссии'),
    ('nurse_surgical', 'Медицинская сестра хирургического отделения'),
    ('nurse_ent', 'Медицинская сестра отоларингологического отделения'),
    ('nurse_procedural', 'Медицинская сестра процедурного кабинета'),
    ('nurse_neurological', 'Медицинская сестра неврологического отделения'),
    ('nurse_dermatological', 'Медицинская сестра кожно-венерологического отделения'),
    ('nurse_dispensary', 'Медицинская сестра диспансерного отделения'),
    ('nurse_consultation', 'Медицинская сестра консультативного отделения'),
    ('nurse_hospital', 'Медицинская сестра палатная (постовая) госпитального отделения'),
    ('nurse_physiotherapy', 'Медицинская сестра физиотерапевтического отделения'),
    ('nurse_functional_diagnostics', 'Медицинская сестра отделения функциональной диагностики'),
    ('nurse_operating', 'Медицинская сестра операционного отделения'),
    ('nurse_urology', 'Медицинская сестра урологического отделения'),
    ('nurse_cardiology', 'Медицинская сестра кардиологического отделения'),
    ('nurse_neonatal', 'Медицинская сестра отделения реанимации новорожденных'),
    ('nurse_neonatal_pathology', 'Медицинская сестра отделения патологии новорожденных'),
    ('nurse_transfusion', 'Медицинская сестра отделения трансфузиологии'),
    
    # Лаборанты и санитарки
    ('radiology_technician', 'Рентгенолаборант'),
    ('medical_registrar', 'Медицинский регистратор'),
    ('orderly_surgical', 'Санитарка хирургического отделения'),
    ('orderly_ent', 'Санитарка отоларингологического отделения'),
    ('orderly_procedural', 'Санитарка процедурного кабинета'),
    ('orderly_neurological', 'Санитарка неврологического отделения'),
    ('orderly_consultation', 'Санитарка консультативного отделения'),
    ('orderly_dispensary', 'Санитарка диспансерного отделения'),
    ('orderly_hospital', 'Санитарка госпитального отделения'),
    ('orderly_operating', 'Санитарка операционного отделения'),
]


    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True,null=True)
    photo = models.ImageField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    role = models.CharField(max_length=50, choices=SPECIALTIES, verbose_name="Должность")
    department = models.CharField(max_length=90,choices=DEPARTMENT_CHOICES,blank=True,null=True,verbose_name='Department')

    def __str__(self):
        return f'Profile of {self.user.username} ({self.get_role_display()} - {self.get_department_display()})'