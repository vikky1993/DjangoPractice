# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class ContactForm(models.Model):
	name		 = models.CharField(max_length=120)
	email		 = models.EmailField(max_length=120, null=True, blank=True)
	# phone_regex  = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
 #    phone_number = models.CharField(validators=phone_regex, max_length=17, blank=True)
	subject	   	 = models.CharField(max_length=120, null=True, blank=True)

	def __str__(self):
		return self.name