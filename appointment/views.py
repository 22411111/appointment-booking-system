from django.shortcuts import render,redirect,get_object_or_404
from .forms import AppointmentForm
from .models import Appointment


# Create your views here.

def home(request):
    return render (request, 'appoinment/home.html')

def appointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    
    else:
        form = AppointmentForm()
      

    context = {
        "form":form
    }

    return render (request, "appointment/appointment.html", context)

def details(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    context = {
        "appointment": appointment,
    }
    return render(request, "appointment/detail.html", context)

def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
     
    if request.method == 'POST': 
        form = AppointmentForm(request.POST, instance=appointment)

        if form.is_valid():
            form.save
            return redirect('details', appointment_id=appointment.id)
        
    else:
        form = AppointmentForm(instance=appointment)
 
    context = {
        "appointment": appointment,
        "form":form, 
    }

    return render (request, "appointment/update.html",context) 

