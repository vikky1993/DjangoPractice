# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateContactForm
from .models import ContactForm


def forms_createview(request):
	form = CreateContactForm()
	if request.method == "POST":
		# name    = request.POST.get("name")
		# email   = request.POST.get("email")
		# subject = request.POST.get("subject")
		form = CreateContactForm(request.POST)
		if form.is_valid():
			obj = ContactForm.objects.create(
					name = form.cleaned_data.get('name'),
					email = form.cleaned_data.get('email'),
					subject = form.cleaned_data.get('subject')

				)
			return HttpResponseRedirect("/")
		if form.errors:
			print(form.errors)
	template_name = 'forms/form.html'
	context = {"form": form}
	return render(request, template_name, context)


def home(request):
	num = random.randint(0, 100000)
	some_list = [num, random.randint(0, 100000), random.randint(0, 100000)]
	context = {
		"bool_item" : True, 
		"num": num,
		"some_list": some_list
	}
	return render(request, "base.html", context)