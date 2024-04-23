from django.shortcuts import render
from .models import ContactDetail,ContactForm


def contact_us(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contactus_form = ContactForm(name=name,subject=subject,email=email,message=message)
        contactus_form.save()

    contactus_list = ContactDetail.objects.all()
    context={
        'contactus_list': contactus_list
    }
    return render(request, "contactus.html", context)
