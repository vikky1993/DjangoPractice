from django import forms

from .models import ContactForm

class Contact(forms.ModelForm):
	email = forms.EmailField(label='', 
		widget=forms.EmailInput(
			attrs={
				'placeholder':'Your email',
				'class': 'form-control'
				}
			))
	class Meta:
		model  = ContactForm
		fields = [
				'name',
				'email',
				'subject',
		]


def clean_email(self, *args, **kwargs):
	email = self.cleaned_data.get("email")
	print(email)
	qs = ContactForm.objects.filter(email__iexact=email)
	if qs.exists():
		raise forms.ValidationError("This email already exists")
	return email