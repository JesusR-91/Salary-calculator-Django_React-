from django.urls import path
from .  import views

urlpatterns = [
    path("netSalary", views.calculate_net_salary),
    path("payroll", views.calculate_payroll)
]

# Backend urls: 
    # http://localhost:8000/netSalary
    # http://localhost:8000/payroll

