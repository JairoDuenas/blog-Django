from django import forms

class FormContact(forms.Form):
  name = forms.CharField(label='Nombre* ', max_length=100, required=True, widget= forms.TextInput(attrs={'placeholder':'Enter your name', 'class':'form-control my-2'}))
  email = forms.CharField(label='Email* ', max_length=100, widget= forms.EmailInput(attrs={'placeholder':'name@example.com', 'class':'form-control my-2'}))
  content = forms.CharField(label='Contenido* ', max_length=100, widget= forms.Textarea(attrs={'placeholder':'Write your comment', 'cols': 30, 'rows': 5, 'class':'form-control my-2'}))
