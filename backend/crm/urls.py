from django.urls import path
from .views import customer_list

app_name='crm'

urlpatterns = [
    path('', customer_list, name='customer_list'),
]
