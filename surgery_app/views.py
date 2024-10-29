from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Doctor, Surgery,Patient
from django.shortcuts import render

# Create your views here.
class DoctorListView(ListView):
    model = Doctor
    template_name = 'dlist.html'
    context_object_name = 'all_ds_list'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'd_detail.html'

class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'd_create.html'
    fields = ['name', 'surgery', 'num_patients']

class DoctorUpdateView(UpdateView):
    model = Doctor
    template_name = 'd_edit.html'
    fields = ['num_patients']

class DPListView(ListView):
    model = Surgery
    template_name = 'sd_list.html'
    context_object_name = 'all_s_list'

def query1(request):
    # Initialize an empty context to pass to the template
    context = {
        'patient_name': None,
        'error_message': None,
    }

    try:
        oldest_patient = Patient.objects.earliest('dob')
        context['patient_name'] = oldest_patient.name

    except Patient.DoesNotExist:
        context['error_message'] = "No patients found."
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query1.html', context)

def query2(request):
    # Initialize an empty context to pass to the template
    context = {
        'name':None,
        'num_patients': None,
        'error_message': None,
    }

    try:
        riverside_surgery = Surgery.objects.get(name="Riverside Clinic")
        number = Patient.objects.filter(surgery=riverside_surgery).count()
        context['num_patients'] = number
        context['name'] = riverside_surgery.name

    except Surgery.DoesNotExist:
        context['error_message'] = "No surgery found."
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query2.html', context)


