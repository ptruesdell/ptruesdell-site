from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    senderEmail = forms.EmailField()
    senderName = forms.CharField(label='Name', max_length=100)