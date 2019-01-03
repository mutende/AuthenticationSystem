from django.contrib.auth.forms import UserCreationForm,  UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


class EditChangePasswordForm(PasswordChangeForm):
	class Meta:
		fields = ('old_password','newpassword1','newpassword2')
	def __init__(self, *args, **kwargs):
		super(EditChangePasswordForm, self).__init__(*args, **kwargs)
		self.fields['old_password'].widget.attrs['class'] = 'form-control'
		self.fields['old_password'].label=''
		self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].label=''
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['new_password1'].help_text='<ul class="form-text text-muted small"><li> Your password can\'t be too similar to your other personal information.</li> <li>Your password must contain at least 8 characters.</li> <li>Your password can\'t be a commonly used password.</li> <li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].label=''
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].help_text='<span class="form-text text-muted"><span><small>Enter the same password as before, for verification.</small></span>'

class EditProfileForm(UserChangeForm):
	password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','email','password')
	def __init__(self, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		# self.fields['username'].label='User Name'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
		

		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		# self.fields['first_name'].label=''
		self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'

		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		# self.fields['first_name'].label=''
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'

		self.fields['email'].widget.attrs['class'] = 'form-control'
		# self.fields['first_name'].label=''
		self.fields['email'].widget.attrs['placeholder'] = 'Email'




class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','email', 'password1','password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].label=''
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
		
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].label=''
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].help_text='<ul class="form-text text-muted small"><li> Your password can\'t be too similar to your other personal information.</li> <li>Your password must contain at least 8 characters.</li> <li>Your password can\'t be a commonly used password.</li> <li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].label=''
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].help_text='<span class="form-text text-muted"><span><small>Enter the same password as before, for verification.</small></span>'