from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import View, FormView, CreateView
from django.shortcuts import render_to_response
from django.template import RequestContext

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

class ContactView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "templates/contact.html", {})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response