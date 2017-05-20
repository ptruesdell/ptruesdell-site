from django.shortcuts import render, get_object_or_404

from contact_form.models import ContactForm

# Create your views here.
def contact_form(request):
	# get the contact form data that is available
	contact_form = get_object_or_404(ContactForm)

	# return the rendered template
	return render(request, 'contact_form/contact_card.html', {'contact_form':contact_form})
