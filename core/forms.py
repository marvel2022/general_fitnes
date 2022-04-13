from django import forms
from django.contrib import messages
# from django.contrib import messages
import phonenumbers

class CantactForm(forms.Form):
	name         = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'type':"text", 'class':"form-control mt-2", 'placeholder':"Введите ваше имя ..."}))
	phone_number = forms.CharField(max_length=13, widget=forms.TextInput(attrs={'type':"text", 'min':"1", 'class':"form-control mt-2 mb-2", 'placeholder':"Ведите свой телефон ...(+998)"}))
	message      = forms.CharField(required=True, widget=forms.Textarea(attrs={'name':"", 'id':"", 'class':"p-3", 'style':"width: 100%;", 'placeholder':"Сообщение...", 'rows':"7"}))
	
	def clean_phone_number(self):
		phone_number = self.cleaned_data.get('phone_number')
		if phone_number.startswith('+998'):
			z = phonenumbers.parse(phone_number, "UZB")
			print("Phone Number: ", phonenumbers.is_valid_number(z))
			if not phonenumbers.is_valid_number(z):
				raise forms.ValidationError("Country code or phone number format didn't match :( \nUse this format +998000000000")
		else:
			raise forms.ValidationError("Phone number doesnt match valid fomat :( \nUse this format +998000000000")
		return phone_number
	
	
	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError("This field must be filled!")
		return name
	
	def clean_message(self):
		message = self.cleaned_data.get('message')
		if not message:
			raise forms.ValidationError("This field must be filled!")
		return message
