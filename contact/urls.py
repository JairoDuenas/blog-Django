from django.urls import path
from contact import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.contact , name='contact'),
]