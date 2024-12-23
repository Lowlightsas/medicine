# Generated by Django 4.1.13 on 2024-12-10 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_alter_profile_role'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitalizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admession_date', models.DateField(verbose_name='Дата поступления')),
                ('department', models.CharField(choices=[('surgery', 'Хирургическое отделение'), ('urology', 'Урологическое отделение'), ('ent', 'Отоларингологическое отделение'), ('maxillofacial', 'Отделение челюстно–лицевой хирургии'), ('traumatology', 'Травматологическое отделение'), ('neurosurgery', 'Нейрохирургическое отделение'), ('ophthalmology', 'Офтальмологическое отделение'), ('anesthesia', 'Отделение анестезиологии и реанимации'), ('operating_room', 'Операционное отделение'), ('angiography', 'Отделение рентген-ангио-хирургических методов диагностики и лечения'), ('transfusion', 'Отделение трансфузиологии (переливания крови)'), ('maternity', 'Родильное отделение'), ('neonatal_reanimation', 'Отделение реанимации новорожденных'), ('neonatal_pathology', 'Отделение патологии новорожденных и выхаживания недоношенных'), ('cardiology', 'Кардиологическое отделение'), ('cardiovascular_surgery', 'Отделение сердечно-сосудистой хирургии'), ('neurology', 'Неврологическое отделение с инсультным центром'), ('diagnostic_center', 'Клинико-диагностический центр'), ('pathology', 'Патологоанатомическое отделение'), ('gynecology', 'Гинекологическое отделение'), ('rehabilitation', 'Отделение восстановительного лечения и медицинской реабилитации')], max_length=50, verbose_name='Отделение')),
                ('reason_for_admission', models.TextField(verbose_name='Причина поступления')),
                ('discharge_date', models.DateField(verbose_name='Дата выписки')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('assigned_doctor', models.ForeignKey(blank=True, limit_choices_to={'role__startswith': 'doctor'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospitalizations_doctor', to='account.profile', verbose_name='Лечащий врач')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospitalizations_patients', to='patients.patients')),
            ],
        ),
    ]
