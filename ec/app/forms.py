from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,  UsernameField, PasswordChangeForm, SetPasswordForm ,PasswordResetForm
from django.contrib.auth.forms import User
from .models import Customer
from django.core.validators import RegexValidator



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})) 
    

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'})) 

    class Meta:
        model = User
        fields =['username','email','password1','password2']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


# class CustomerProfileForm(forms.ModelForm):
#     mobile = forms.CharField(validators=[RegexValidator(regex='^[0-9]{10}$', message='Enter a valid 10 digit mobile number.')], max_length=10, widget=forms.TextInput(attrs={'class':'form-control', 'error_messages': {'invalid': 'Please enter a 10 digit mobile number.'}}))
#     zipcode = forms.CharField(validators=[RegexValidator(regex='^[0-9]{6}$', message='Enter a valid pincode number.')], max_length=6,widget=forms.TextInput(attrs={'class':'form-control', 'error_messages': {'invalid':'Please enter a valid pincode.'}}))

#     class Meta:
#         model = Customer
#         fields=['name','address','locality','city','mobile','state','zipcode']
#         widgets={
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'address':forms.TextInput(attrs={'class':'form-control'}),
#             'locality':forms.TextInput(attrs={'class':'form-control'}),
#             'city':forms.TextInput(attrs={'class':'form-control'}),
#             # 'mobile':forms.NumberInput(attrs={'class':'form-control'}),
#             'state':forms.Select(attrs={'class':'form-control'}),
#             # 'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
#         }

class CustomerProfileForm(forms.ModelForm):
    mobile = forms.CharField(
        validators=[RegexValidator(regex='^[0-9]{10}$', message='Enter a valid 10 digit mobile number.')],
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'error_messages': {'invalid': 'Please enter a 10 digit mobile number.'}}),
        required=True  # Set the field as required
    )
    zipcode = forms.CharField(
        validators=[RegexValidator(regex='^[0-9]{6}$', message='Enter a valid pincode number.')],
        max_length=6,
        widget=forms.TextInput(attrs={'class': 'form-control', 'error_messages': {'invalid': 'Please enter a valid pincode.'}}),
        required=True  # Set the field as required
    )

    class Meta:
        model = Customer
        fields = ['name', 'address', 'locality', 'city', 'mobile', 'state', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.required:
                field.widget.attrs['required'] = True
                field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' required-field'










