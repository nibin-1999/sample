from django.urls import path
from .views import country_list

app_name = 'main'

urlpatterns = [
    path('countries/', country_list, name='country-list'),
]
