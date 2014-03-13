from django import forms
from game.models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), help_text="Please enter a username.")
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), help_text="Please enter a password.")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
	
    	about = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), help_text="About yourself", required=False)
	picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

    	class Meta:
        	model = UserProfile
        	fields = ('about', 'picture')
