from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage


from contact_form.models import ContactInfo
from contact_form.forms import ContactForm

# Contact form view
def contact(request):
	# if this is a POST request, we need to process the data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = ContactForm(request.POST)
		# check whether it is valid
		if form.is_valid():
		    subject = form.cleaned_data['subject']
		    message = form.cleaned_data['message']
		    senderEmail = form.cleaned_data['senderEmail']
		    senderName = form.cleaned_data['senderName']
		    recipients = ['parkertruesdell@gmail.com']
		    print("trying to send email")
		    send_mail(subject, message, senderEmail, recipients, fail_silently=False)
		return HttpResponseRedirect('')

	# if this is a GET request, render a blank contact form
	else:
		contact_info = get_object_or_404(ContactInfo)

		# get the form
		form = ContactForm()

		# render contact info and form
		return render(request, 'contact_form/contact_card.html', {'form':form, 'contact_info':contact_info})


