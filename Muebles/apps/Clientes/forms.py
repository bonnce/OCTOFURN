from django import forms
from . import models
from django.utils.translation import gettext_lazy as _

class ClientForm(forms.ModelForm):
    class Meta:
        model=models.Clientes
        fields = ['first_name','last_name','phone','direction']
        labels = {
            'first_name': _('Nombre'),
            'last_name': _('Apellido'),
            'phone': _('Telefono'),
            'direction': _('Direccion')
        }