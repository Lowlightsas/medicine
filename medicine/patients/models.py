from django.db import models

class Patients(models.Model):
    
    GENDER_CHOICES = [('male','MALE'),
                      ('female','FEMALE')]
    
    REGION_CHOICES = [
    ('abay', 'Абайская область'),
    ('akmola', 'Акмолинская область'),
    ('aktobe', 'Актюбинская область'),
    ('almaty_region', 'Алматинская область'),
    ('atyrau', 'Атырауская область'),
    ('east_kazakhstan', 'Восточно-Казахстанская область'),
    ('zhambyl', 'Жамбылская область'),
    ('zhetisu', 'Жетысуская область'),
    ('west_kazakhstan', 'Западно-Казахстанская область'),
    ('karaganda', 'Карагандинская область'),
    ('kostanay', 'Костанайская область'),
    ('kyzylorda', 'Кызылординская область'),
    ('mangystau', 'Мангистауская область'),
    ('turkistan', 'Туркестанская область'),
    ('north_kazakhstan', 'Северо-Казахстанская область'),
    ('ulytau', 'Улытауская область'),
    ('astana', 'Астана (город республиканского значения)'),
    ('almaty', 'Алматы (город республиканского значения)'),
    ('shymkent', 'Шымкент (город республиканского значения)'),]

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
    
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    middle_name = models.CharField(max_length=30,blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,verbose_name='пол')
    contact_number = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=100,blank=True)
    region = models.CharField(max_length=50,choices=REGION_CHOICES,verbose_name='Регион проживания')
    iin = models.CharField(max_length=12,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    department = models.CharField(max_length=50,choices=DEPARTMENT_CHOICES,verbose_name='отделение пациента')

    
    def __str__(self):
        return f'{self.department} - {self.first_name} {self.last_name} {self.middle_name}'