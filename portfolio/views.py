from django.shortcuts import render
from portfolio.models import Projects

# Create your views here.

def portfolio(request):
  projects = Projects.objects.all()
  return render(request, 'portfolio/portfolio.html', {'projects':projects})