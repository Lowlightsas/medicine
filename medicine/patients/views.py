from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patients
from treatments.models import Treatments
from medical_records.models import MedicalRecords

@login_required
def patient_list(request):
    patients = Patients.objects.all()

    return render(request,'patient_list.html',{'patients':patients})

@login_required
def patient_detail(request, patient_id):
   
    patient = get_object_or_404(Patients, id=patient_id)

    # Фильтруем записи лечения, относящиеся к этой карте
    treatments = Treatments.objects.all()
    context = {
        'patient': patient,
       
        'treatments':treatments,
    }
    
    return render(request, 'patient_detail.html', context)