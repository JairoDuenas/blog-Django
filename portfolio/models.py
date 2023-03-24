from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Projects(models.Model):
  image = models.ImageField(upload_to='portfolio', null=True, blank=True)
  title = models.CharField(max_length=50)
  description = models.TextField(blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  link = models.CharField(max_length=200, default='')
  link_git = models.CharField(max_length=200, default='')

  class Meta:
    verbose_name='project'
    verbose_name_plural='projects'

  def __str__(self):
    return self.title