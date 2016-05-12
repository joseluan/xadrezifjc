# -*- coding:utf-8 -*-
from django import forms
from django.forms import CharField, Form, PasswordInput,ModelForm
from django.contrib.admin import widgets         
from django.contrib.auth.models import User
from livros.models import *
from django.contrib.admin.widgets import AdminFileWidget

class FormFotoCliente(forms.Form):
	file = forms.FileField(label='Buscar foto') 

