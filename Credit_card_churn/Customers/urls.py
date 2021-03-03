from django.urls import path
from .views import ViewCustomerData, SaveCustomerData

urlpatterns = [
    path('customers', ViewCustomerData.as_view(), name='fetch_customer'),
    path('save_customers/',SaveCustomerData, name='save_customer'),
]