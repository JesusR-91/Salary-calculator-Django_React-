from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Employee, SocialSecurityDeductions, Payroll
from rest_framework.response import Response


# Net Salary
@api_view(["POST"])
def calculate_net_salary(request):

    """
    Request data structure:

        Mandatory data:
            - name
            - salary_base
            - community
        
        Optional data
            - health_insurance
            - complements = {k:v, ...}
            - pro_rate_extra_payments
            - extra_hours
            - sickness_day 
            
    """

    # Employee Object
    employee = Employee(
        #Mandatory values
        salary_base=request.data['salary_base'],
        community=request.data['community'],

        #Optional values

        health_insurance=request.data.get('health_insurance', None),
        complements=request.data.get('complements', None),
        pro_rate_extra_payments=request.data.get('pro_rate_extra_payments', None),
        extra_hours=request.data.get('extra_hours', None),
        sickness_day=request.data.get('sickness_day', None)
    )

    social_security_deductions = SocialSecurityDeductions(employee).calculate_deductions()
    payroll = Payroll(employee, social_security_deductions)
    
    return Response({"net_salary": payroll.calculate_net_salary()})

#Payroll

@api_view(["POST"])
def calculate_payroll(request):

    employee = Employee(
        #Mandatory values
        salary_base=request.data['salary_base'],
        community=request.data['community'],

        #Optional values
        health_insurance=request.data.get('health_insurance', None),
        complements=request.data.get('complements', None),
        pro_rate_extra_payments=request.data.get('pro_rate_extra_payments', None),
        extra_payments=request.data.get('extra_payments', None),
        extra_hours=request.data.get('extra_hours', None),
        sickness_day=request.data.get('sickness_day', None)
    )

    social_security_deductions = SocialSecurityDeductions(employee).calculate_deductions()
    payroll = Payroll(employee, social_security_deductions)
    
    return Response(payroll.calculate_payroll())