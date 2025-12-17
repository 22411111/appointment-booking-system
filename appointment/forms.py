from django import forms
from .models import appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = "__all__"