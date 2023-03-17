from django.shortcuts import render, redirect
from .forms import FormContact
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
  form_contact = FormContact()
  if request.method == 'POST':
    form_contact = FormContact(data=request.POST)
    if form_contact.is_valid():
      name = request.POST.get('name')
      email = request.POST.get('email')
      content = request.POST.get('content')

      email = EmailMessage("Mensaje desde contacto backend", f"El usuario con nombre {name} con correo electrónico {email} escribe lo siguiente: \n\n {content}", "", ["jairo251180@gmail.com"], reply_to=[email])

      try:
        email.send()
        return redirect("/contact/?valid")
      except:
        return redirect("/contact/?novalid")

  return render(request, 'contact/contact.html', {'my_form':form_contact})