from django.urls import path
#from . import views
from .views import VRegistro, cerrar_cesion, logear

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', VRegistro.as_view(), name='autenticacion'),
    path('cerrar_cesion', cerrar_cesion, name='cerrar_cesion'),
    path('logear', logear, name='logear'),

]