from django.db import models

# Create your models here.
class ContactForm(models.Model):
	firstName = models.CharField(max_length=255)
	lastName = models.CharField(max_length=255)
	phoneNumber = models.CharField(max_length=16)
	email = models.CharField(max_length=255)
	githubProfile = models.CharField(max_length=255)
	linkedinProfile = models.CharField(max_length=255)
	pgpPublicKey = models.TextField(default="")