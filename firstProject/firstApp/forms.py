from django import forms
from .models import RentCar

# class ReservationForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = '__all__'

class RentCarForm(forms.ModelForm):
    class Meta:
        model = RentCar
        fields = '__all__'