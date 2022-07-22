from fileinput import filename
from django.shortcuts import render
from .models import ConsultationList
from django.views.generic import CreateView
from .forms import ConsultationForm

from django.http import FileResponse, HttpResponse, HttpResponseRedirect
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus.paragraph import Paragraph

# Create your views here.

def download_pdf(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ConsultationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            buf =io.BytesIO()
            c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
            textob=c.beginText()
            textob.setTextOrigin(inch,inch)
            textob.setFont("Helvetica",14)
            lines=[]
            clinic_name = form.cleaned_data['clinic_name']
            clinic_logo = form.cleaned_data['clinic_logo']            
            phys_name = form.cleaned_data['physician_name']
            phys_contcat = form.cleaned_data['physician_contact']
            pt_first_name = form.cleaned_data['pt_first_name']
            pt_last_name = form.cleaned_data['pt_last_name']
            pt_dob = form.cleaned_data['pt_dob']
            pt_contact = form.cleaned_data['pt_contact']
            chief_Complaint= form.cleaned_data['chief_complaint']
            consultation_Note= form.cleaned_data['consultation_note']

            fileName = "CR_{0}_{1}_{2}.pdf".format(pt_first_name,pt_last_name,pt_dob)
            lines.append(f"Clinic Name: {clinic_name} ")
            lines.append(f"Clinic Logo: {clinic_logo}")
            lines.append(f"Physician Name: Dr. {phys_name}") 
            lines.append(f"Physician Contact: {phys_contcat}")
            lines.append(f"Patient First Name: {pt_first_name}")
            lines.append(f"Patient Last Name: {pt_last_name}")
            lines.append("Patient Dob: {}".format(pt_dob.strftime("%d-%b-%y")))
            lines.append(f"Patient Contact: {pt_contact}")
            lines.append(f"Chief Complaint: {chief_Complaint}")
            lines.append(f"Consultation Note: {consultation_Note}")
 
            for line in lines:
                textob.textLine(line )
                textob.textLine("")

            c.drawText(textob)
            c.showPage()
            c.save()
            buf.seek(0)    
            return FileResponse(buf,as_attachment=True,filename=fileName)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ConsultationForm()

    return render(request, 'home.html', {'form': form})
