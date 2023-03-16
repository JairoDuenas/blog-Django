from django.urls import path
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)