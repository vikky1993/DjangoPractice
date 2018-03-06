from django import forms


class CreateContactForm(forms.Form):
	name		 = forms.CharField()
	email		 = forms.EmailField()
	subject	   	 = forms.CharField(required=False)
