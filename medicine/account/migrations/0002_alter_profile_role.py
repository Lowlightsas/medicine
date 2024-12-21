# Generated by Django 4.1.13 on 2024-12-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('cardiologist', 'Врач-кардиолог'), ('otolaryngologist', 'Врач-отоларинголог'), ('therapist', 'Врач-терапевт'), ('hospital_therapist', 'Врач-терапевт госпитального отделения'), ('manual_therapy', 'Врач мануальной терапии'), ('reflexologist_neurologist', 'Врач-рефлексотерапевт-невролог'), ('psychiatrist', 'Врач-психиатр'), ('psychiatrist_narcologist', 'Врач-психиатр-нарколог'), ('hematologist', 'Врач-гематолог'), ('rheumatologist', 'Врач-ревматолог'), ('ophthalmologist', 'Врач-офтальмолог'), ('urologist', 'Врач-уролог'), ('gynecologist', 'Врач-акушер-гинеколог'), ('dermatologist', 'Врач-дерматовенеролог'), ('diagnostics_doctor', 'Врач функциональной диагностики'), ('feldsher_commission', 'Фельдшер военно-врачебной комиссии'), ('nurse_commission', 'Медицинская сестра военно-врачебной комиссии'), ('nurse_surgical', 'Медицинская сестра хирургического отделения'), ('nurse_ent', 'Медицинская сестра отоларингологического отделения'), ('nurse_procedural', 'Медицинская сестра процедурного кабинета'), ('nurse_neurological', 'Медицинская сестра неврологического отделения'), ('nurse_dermatological', 'Медицинская сестра кожно-венерологического отделения'), ('nurse_dispensary', 'Медицинская сестра диспансерного отделения'), ('nurse_consultation', 'Медицинская сестра консультативного отделения'), ('nurse_hospital', 'Медицинская сестра палатная (постовая) госпитального отделения'), ('nurse_physiotherapy', 'Медицинская сестра физиотерапевтического отделения'), ('nurse_functional_diagnostics', 'Медицинская сестра отделения функциональной диагностики'), ('radiology_technician', 'Рентгенолаборант'), ('medical_registrar', 'Медицинский регистратор'), ('orderly_surgical', 'Санитарка хирургического отделения'), ('orderly_ent', 'Санитарка отоларингологического отделения'), ('orderly_procedural', 'Санитарка процедурного кабинета'), ('orderly_neurological', 'Санитарка неврологического отделения'), ('orderly_consultation', 'Санитарка консультативного отделения'), ('orderly_dispensary', 'Санитарка диспансерного отделения'), ('orderly_hospital', 'Санитарка госпитального отделения')], max_length=50, verbose_name='Должность'),
        ),
    ]