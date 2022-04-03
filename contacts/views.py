from django.contrib import messages

from contacts.models import Contact
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Thank you,Our representative will contact you soon.')

    return render(request,'contacts/contacts.html')