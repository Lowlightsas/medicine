# Generated by Django 4.1.13 on 2024-12-08 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='')),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(choices=[('doctor', 'Doctor'), ('nurse', 'Nurse')], max_length=30)),
                ('department', models.CharField(blank=True, choices=[('surgery', 'Хирургическое отделение'), ('urology', 'Урологическое отделение'), ('ent', 'Отоларингологическое отделение'), ('maxillofacial', 'Отделение челюстно–лицевой хирургии'), ('traumatology', 'Травматологическое отделение'), ('neurosurgery', 'Нейрохирургическое отделение'), ('ophthalmology', 'Офтальмологическое отделение'), ('anesthesia', 'Отделение анестезиологии и реанимации'), ('operating_room', 'Операционное отделение'), ('angiography', 'Отделение рентген-ангио-хирургических методов диагностики и лечения'), ('transfusion', 'Отделение трансфузиологии (переливания крови)'), ('maternity', 'Родильное отделение'), ('neonatal_reanimation', 'Отделение реанимации новорожденных'), ('neonatal_pathology', 'Отделение патологии новорожденных и выхаживания недоношенных'), ('cardiology', 'Кардиологическое отделение'), ('cardiovascular_surgery', 'Отделение сердечно-сосудистой хирургии'), ('neurology', 'Неврологическое отделение с инсультным центром'), ('diagnostic_center', 'Клинико-диагностический центр'), ('pathology', 'Патологоанатомическое отделение'), ('gynecology', 'Гинекологическое отделение'), ('rehabilitation', 'Отделение восстановительного лечения и медицинской реабилитации')], max_length=90, null=True, verbose_name='Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
