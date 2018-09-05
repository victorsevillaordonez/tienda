from django import forms
from .models import Producto
from django.contrib.auth.models import User

class agregar_producto_form(forms.ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'

class login_form(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput())
	clave = forms.CharField(widget=forms.PasswordInput(render_value=False))

class registro_usuario(forms.Form):
	"""docstring for registro_usuario"""
	usuario = forms.CharField(widget=forms.TextInput)
	email = forms.EmailField(widget=forms.TextInput)
	password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(render_value=False))
	password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		usuario = self.cleaned_data['username']
		try:
			u = User.objects.get(usuario=usuario)
		except User.DoesNotExist as e:
			return usuario
		raise forms.ValidationError('Nombre de usuario ya registrado')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			email = User.objects.get(email=email)
		except User.DoesNotExist as e:
			return email
		raise forms.ValidationError('Correo electronico ya registrado')

	def clean_password(self):
		password = self.cleaned_data['password1']
		confirmarPassword = self.cleaned_data['password2']

		if password == confirmarPassword:
			pass
		else:
			raise forms.ValidationError('Contaseña no coincide')
		