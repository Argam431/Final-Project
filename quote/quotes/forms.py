from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from quotes.models import Quote, Tag


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control form-control-lg"
            }
        ))

    password = forms.CharField(required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control form-control-lg"
            }
        ))






class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                'id':"form3Example1cg",
                'class':"form-control form-control-lg",
            }
        ))


    first_name = forms.CharField(required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First name",                
                'id':"form3Example1cg",
                'class':"form-control form-control-lg",
            }
        ))   
   
    
    last_name = forms.CharField(required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last name", 
                'id':"form3Example1cg",
                'class':"form-control form-control-lg",

            }
        )) 
                
    password1 = forms.CharField(required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                'id':"form3Example4cg",
                'class':"form-control form-control-lg",
            }
        ))
    password2 = forms.CharField(required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Repeat your password",
                'id':"form3Example4cdg",
                'class':"form-control form-control-lg",
            }
        ))

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2')


class CreateQuoteForm(forms.ModelForm):
       
    class Meta:
        model = Quote
        fields = '__all__'
        exclude = ('author',)

    tags = forms.ModelMultipleChoiceField(Tag.objects.order_by('name'),required=True,help_text='Please enter the [ctrl] for Multiple Choice')

