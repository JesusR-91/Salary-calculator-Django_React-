import json

class Employee:
    def __init__(self, salary_base, community, health_insurance=None, complements=None, pro_rate_extra_payments=None,extra_payments=None, extra_hours=None, sickness_day=None):
        self.salary_base = int(salary_base)
        self.complements = complements
        self.pro_rate_extra_payments = pro_rate_extra_payments
        self.extra_payments = extra_payments
        self.extra_hours = extra_hours
        self.health_insurance = health_insurance
        self.community = community
        self.sickness_day = sickness_day
        
    def calculate_irpf(self):

        if self.complements is not None:
            complements_json = self.complements
            complements = sum(complements_json.values())
        else:
            complements = 0
        
        #Conditional to check if there is an extra payment or it is pro-rated
        if self.pro_rate_extra_payments :
            extra = self.pro_rate_extra_payments 
        elif self.extra_payments :
            extra = self.extra_payments
        else:
            extra = (self.salary_base / 12 )/ 6


        salary_base = self.salary_base + (complements * 12) + extra

        base_after_irpf = 0
        previous_section = 0

        if (self.community == "Andalucía"):
            irpf = {
                12450: 0.19,
                13000: 0.215,
                20200: 0.24,
                21000: 0.27,
                35200: 0.30,
                60000: 0.37,
                300000: 0.45,
                300001: 0.47
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
            
        if (self.community == "Aragón"):
            irpf = {
                12450: 0.19,
                13972.5: 0.215,
                20200: 0.24,
                21210: 0.27,
                35200: 0.30,
                36960: 0.3,
                52500: 0.37,
                60000: 0.39,
                80000: 0.455,
                90000: 0.465,
                130000: 0.475,
                300000: 0.48,
                300001: 0.50
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "Asturias"):
            irpf = {
                12450: 0.19,
                17707: 0.24,
                20200: 0.26,
                33007: 0.29,
                35200: 0.335,
                53407: 0.37,
                60000: 0.40,
                70000: 0.44,
                90000: 0.45,
                175000: 0.475,
                300000: 0.48,
                300001: 0.50
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
                
        if(self.community == "Baleares"):
            irpf = {
                10000: 0.185,
                12450: 0.2075,
                18000: 0.2325,
                20200: 0.2625,
                30000: 0.2925,
                35200: 0.325,
                48000: 0.36,
                60000: 0.375,
                70000: 0.415,
                90000: 0.4425,
                120000: 0.4525,
                175000: 0.4625,
                300000: 0.4725,
                300001: 0.50
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "Canarias"):
            irpf = {
                12450: 0.185,
                17707: 0.21,
                20200: 0.26,
                33007: 0.29,
                35200: 0.335,
                53407: 0.37,
                60000: 0.42,
                90000: 0.46,
                120000: 0.475,
                300000: 0.485,
                300001: 0.505
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "Cantabria"):
            irpf = {
                12450: 0.185,
                13000: 0.205,
                20200: 0.23,
                21000: 0.26,
                35200: 0.295,
                60000: 0.365,
                90000: 0.45,
                300000: 0.47,
                300001: 0.49
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "Castilla la Mancha"):
            irpf = {
                12450: 0.19,
                20200: 0.24,
                35200: 0.30,
                60000: 0.37,
                300000: 0.45,
                300001: 0.47
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "Castilla y León"):
            irpf = {
                12450: 0.185,
                20200: 0.24,
                35200: 0.29,
                53407: 0.37,
                60000: 0.40,
                300000: 0.44,
                300001: 0.46
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "Cataluña"):
            irpf = {
                12450: 0.20,
                17707: 0.24,
                20200: 0.26,
                21000: 0.29,
                33007: 0.30,
                35200: 0.338,
                53407: 0.373,
                60000: 0.40,
                90000: 0.44,
                120000: 0.46,
                175000: 0.47,
                300000: 0.48,
                300001: 0.50
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "Comunidad de Madrid"):
            irpf = {
                12450: 0.18,
                13362: 0.205,
                18004: 0.227,
                20200: 0.248,
                35200: 0.278,
                35425: 0.313,
                57320: 0.359,
                60000: 0.39,
                300000: 0.43,
                300001: 0.45
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
                
        if(self.community == "Comunidad Valenciana"):
            irpf = {
                12000: 0.185,
                12450: 0.215,
                20200: 0.24,
                22000: 0.27,
                32000: 0.30,
                35200: 0.325,
                42000: 0.36,
                52000: 0.385,
                60000: 0.41,
                65000: 0.45,
                72000: 0.475,
                100000: 0.47,
                150000: 0.50,
                200000: 0.51,
                300000: 0.52,
                300001: 0.55
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "Extremadura"):
            irpf = {
                12450: 0.175,
                20200: 0.22,
                24200: 0.31,
                35200: 0.325,
                60000: 0.395,
                80200: 0.46,
                99200: 0.465,
                120200: 0.47,
                300000: 0.475,
                300001: 0.495
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "Galicia"):
            irpf = {
                12450: 0.185,
                12985: 0.21,
                20200: 0.2365,
                21068: 0.2665,
                35200: 0.299,
                47600: 0.369,
                60000: 0.369,
                300000: 0.45,
                300001: 0.47
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "La Rioja"):
            irpf = {
                12450: 0.175,
                20200: 0.226,
                35200: 0.286,
                40000: 0.363,
                50000: 0.37,
                60000: 0.375,
                120000: 0.47,
                300000: 0.495,
                300001: 0.515
            }

            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "Murcia"):
            irpf = {
                12450: 0.18,
                20200: 0.232,
                34000: 0.283,
                35200: 0.329,
                60000: 0.364,
                300000: 0.45,
                300001: 0.47
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "Navarra"):
            irpf = {
                4458: 0.13,
                10030: 0.22,
                21175: 0.25,
                35663: 0.28,
                51266: 0.355,
                66869: 0.415,
                89159: 0.44,
                139310: 0.47,
                195034: 0.505,
                334344: 0.54
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf
        
        if(self.community == "País Vasco"):
            irpf = {
                17720: 0.23,
                35440: 0.28,
                53160: 0.35,
                75910: 0.4,
                105130: 0.45,
                140130: 0.46,
                204270: 0.47,
                204271: 0.49
            }
        
            for section, percentage in irpf.items():
                if salary_base < section:
                    base_after_irpf += (salary_base - previous_section) * (1 - percentage)
                    break
                else:
                    base_after_irpf += (section - previous_section) * (1 - percentage)
                    previous_section = section
            
            return salary_base - base_after_irpf

class SocialSecurityDeductions:

    def __init__(self, employee):
        self.employee = employee

    def calculate_deductions(self):

        #Conditional to check if there is an extra payment or it is pro-rated
        if self.employee.pro_rate_extra_payments :
            extra = self.employee.pro_rate_extra_payments 
        elif self.employee.extra_payments :
            extra = self.employee.extra_payments
        else:
            extra = (self.employee.salary_base / 12 )/ 6

        if self.employee.complements is not None:
            complements = sum(self.employee.complements.values())
        else:
            complements = 0

        salary_base = self.employee.salary_base + (complements * 12) + ((self.employee.salary_base /12) *2) #Salary base + complements + extra_payment (2 extra payments yearly)

        # Employee Deductions
        common_contingencies = salary_base * 0.047
        unemployment = salary_base * 0.016
        professional_training = salary_base * 0.001
        intergenerational_equity = salary_base * 0.001

        employee_deductions = {
            "common_contingencies": common_contingencies, 
            "unemployment": unemployment, 
            "professional_training": professional_training, 
            "intergenerational_equity": intergenerational_equity, 
        }

        # Company Deductions
        common_contingencies_company = salary_base * 0.2360
        at_ep = salary_base * 0.02
        unemployment_company= salary_base * 0.055
        professional_training_company = salary_base * 0.006
        fogasa = salary_base * 0.002

        company_deductions = {
            "common_contingencies_company": common_contingencies_company, 
            "at_ep": at_ep, 
            "unemployment_company": unemployment_company, 
            "professional_training_company": professional_training_company, 
            "fogasa": fogasa, 
        }

        #Extra hours checking 
        if self.employee.extra_hours != None:
            extra_hours_employee = self.extra_hours * 0.047
            employee_deductions["extra hours"] = extra_hours_employee
            extra_hours_company = self.extra_hours * 0.236
            company_deductions["extra hours"] = extra_hours_company

        return employee_deductions, company_deductions
        
class Payroll:
    def __init__(self, employee, social_security_deductions):
        self.employee = employee #Object of class Employee
        self.irpf = employee.calculate_irpf()
        self.social_security_deductions = social_security_deductions #The calculate deductions function object structure -> (employee_deductions, company_deductions)

    def calculate_net_salary(self):
        employee_deductions = self.social_security_deductions[0]

        #Conditional to check if there is an extra payment or it is pro-rated
        if self.employee.pro_rate_extra_payments :
            extra = self.employee.pro_rate_extra_payments 
        elif self.employee.extra_payments :
            extra = self.employee.extra_payments
        else:
            extra = (self.employee.salary_base / 12 )/ 6

        if self.employee.complements is not None:
            complements = sum(self.employee.complements.values())
        else:
            complements = 0

        net_salary = (self.employee.salary_base/12 + complements + extra) - (self.irpf/12) - (sum(employee_deductions.values())/12)
        return net_salary

    def calculate_payroll(self):
        employee_deductions = list(self.social_security_deductions[0].values())
        company_deductions = list(self.social_security_deductions[1].values())

        #Formating the complements to get a json object
        if self.employee.complements is not None:
            complements_dict = self.employee.complements
        else: 
            complements_dict = {"No complements added"}

        if self.employee.pro_rate_extra_payments :
            proRatedExtraPayment = self.employee.pro_rate_extra_payments
        else:
            proRatedExtraPayment = (self.employee.salary_base / 12) /6


        payroll = {
            "employee" : {
                "Base salary" : self.employee.salary_base / 12 ,
                "Complements" : complements_dict,
                "Irpf": self.irpf / 12,

                "social security deductions": {
                    "Common contingencies": employee_deductions[0] / 12, 
                    "Unemployment": employee_deductions[1] / 12, 
                    "Professional training": employee_deductions[2] / 12, 
                    "Intergenerational equity": employee_deductions[3] / 12, 
                },

                "Net salary": self.calculate_net_salary()
            },
            "company": {
               "Common contingencies company": company_deductions[0] / 12, 
                "At ep": company_deductions[1] / 12, 
                "Unemployment company": company_deductions[2] / 12, 
                "Professional training company": company_deductions[3] / 12, 
                "Fogasa": company_deductions[4] / 12, 
                "Total company deductions": sum(company_deductions) /12 
            }
        }

        #Optional values
        if self.employee.sickness_day is not None:
            payroll["employee"]["sick leaves"] = self.employee.sickness_day * ((self.employee.salary_base / 12) / 30)
            
        if self.employee.health_insurance is not None:
            payroll["employee"]["Health insurance"] = self.employee.health_insurance

        if self.employee.extra_hours is not None:
            payroll["employee"]["Extra hours"] = self.employee.extra_hours

        if hasattr(self.employee, 'extra_payments') and self.employee.extra_payments is not None:
            payroll["employee"]["Extra payment"] = self.employee.extra_payments
        else:
            payroll["employee"]["Pro-rate extra payment"] = proRatedExtraPayment

        # if self.employee.extra_hours is not None:
        #     payroll["employee"]["Extra hours"] = self.employee.extra_hours
        #     payroll["employee"]["Social security deductions"]["extra hours"] = employee_deductions.extra_hours_employee
        #     payroll["company"]["Extra hours"] = company_deductions.extra_hours_company


        return payroll
    