from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import crtinfo, usrinfo, User,criminfo



class CrtReg(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta(UserCreationForm):
        model = User
        fields = ['id','email','username']

    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_crt = True
        user.save()
        crt = crtinfo.objects.create(user=user)
        return user

class CrimReg(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()
    
    class Meta(UserCreationForm):
        model  = User
        fields = ['id','email','username']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_crim = True
        user.save()
        crim = criminfo.objects.create(user=user)
        return user


class UserReg(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta(UserCreationForm):
        model  = User
        fields = ['id','email','username']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_user = True
        user.save()
        usr = usrinfo.objects.create(user=user)
        return user        