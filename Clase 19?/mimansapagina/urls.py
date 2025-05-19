from django.urls import path
from mimansapagina.views import index

urlpatterns = [
    path('', index, name='indice')
]
