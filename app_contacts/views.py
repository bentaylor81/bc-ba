from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from .models import contact
from .forms import ContactForm
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your message has been sent, a member of our team will reply to you shortly.'))
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            company = request.POST.get("company")
            position = request.POST.get("position")
            address = request.POST.get("address")
            zip_code = request.POST.get("zip_code")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            website = request.POST.get("website")
            membership_type = request.POST.get("membership_type")
            comments = request.POST.get("comments")

            # To email oursevles the messge
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [settings.DEFAULT_FROM_EMAIL]

            context = {
                'first_name': first_name,
                'last_name': last_name,
                'company': company,
                'position': position,
                'address': address,
                'zip_code': zip_code,
                'phone': phone,
                'email': email, 
                'website': website,
                'membership_type': membership_type,
                'comments': comments,
            }

            subject = get_template('app_contacts/contact_subject.txt').render(context)
            contact_message = get_template('app_contacts/contact_message.txt').render(context)

            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
            return redirect("/contact/")
        else: 
            messages.error(request, ('There is an invalid field in the contact form, please try again.'))
            return redirect("/contact/")
    else:
        return render(request, 'app_contacts/contact.html', {} )


