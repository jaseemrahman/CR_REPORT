from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class ConsultationList(models.Model):
    clinic_name=models.CharField(max_length=50)
    clinic_logo=models.CharField(max_length=25)
    physician_name=models.CharField(max_length=50)
    physician_contact=models.CharField(max_length=100)
    pt_first_name=models.CharField(max_length=25)
    pt_last_name=models.CharField(max_length=25)
    pt_dob=models.DateField()
    pt_contact=models.CharField(max_length=100)
    chief_complaint=RichTextField(max_length=5000)
    consultation_note=RichTextField(max_length=5000)

    def __str__(self):
        return self.clinic_name
