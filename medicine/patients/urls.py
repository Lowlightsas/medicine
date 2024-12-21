from django.urls import path
from . import views


app_name = 'patients'

urlpatterns = [
    path('list/',views.patient_list,name='patient_list'),
    path('<int:patient_id>/patient-detail/',views.patient_detail,name='patient_detail'),
]
