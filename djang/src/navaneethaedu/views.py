from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import View, FormView, CreateView

# Create your views here.
from .forms import Contact

# def home(request):
# 	return render(request, "index.html", {})


class HomeView(SuccessMessageMixin, CreateView):
	template_name = 'templates/index.html'
	form_class	  = Contact
	success_url   = '/'

	def get_success_message(self, cleaned_data):
		print(cleaned_data)
		return "Thank you for leaving a message! We will get back to you."

class AboutView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "templates/aboutus.html", {})