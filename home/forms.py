from django import forms
from .models import ConsultationList
from ckeditor.fields import RichTextField 
# from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget

# from django import ModelForm
class Dateinput(forms.DateInput):
    input_type='Date'

class ConsultationForm(forms.Form):
    clinic_name = forms.CharField(max_length=100)
    clinic_logo = forms.CharField(max_length=100)
    physician_name = forms.CharField(max_length=100)
    physician_contact = forms.CharField(max_length=100)
    pt_first_name = forms.CharField(max_length=100)
    pt_last_name = forms.CharField(max_length=100)
    pt_dob  = forms.DateField()
    pt_contact = forms.CharField(max_length=100)
    chief_complaint =  forms.CharField(widget=CKEditorWidget(),max_length=5000)
    consultation_note = forms.CharField(widget=CKEditorWidget(),max_length=5000)

    class Meta:
        widgets = {
            'pt_dob':Dateinput(),
               }

