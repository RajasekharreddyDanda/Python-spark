import json
import numpy as np
import pandas as pd

def get_input_for_interest_calculation(p, t, r):    
    interest_rate = (p + t + r)/100
    return interest_rate

p = 10000
t = 12
r =5
summ_of_intrst = get_input_for_interest_calculation(p,t,r)
print ("Sum of Interest: ", summ_of_intrst)

# date formarts convert functions.  
from datetime import datetime
date_format = "%Y-%m-%d"
today = datetime.now().strftime(date_format)
print ("Today's Date :", today)
# change date format yyyy-mm-dd to mm-dd-yyyy 
formatted_date = datetime.strptime(today, date_format).strftime("%m/%d/%Y")
print("Formatted Date: ", formatted_date)


import numpy as np

class LoanCalculator:
    def __init__(self, principal, time, rate):
        self.principal = float(principal)
        self.time = int(time) * 12  # converting months into years for simplicity
        self.rate = float(rate) / 100  # converting percentage to decimal

    def calculate_monthly_payment(self):
        # calculate monthly payment using the formula for present value of an annuity
        r = self.rate / 12  # monthly interest rate
        n = self.time  # total number of payments
        M = self.principal * (r * (1 + r)**n) / ((1 + r)**n - 1)
        return round(M, 2)

    def calculate_total_amount_paid(self):
        num_of_payments = self.time
        P = np.round(self.calculate_monthly_payment() * num_of_payments, 2)
        return P

myLoan = LoanCalculator(10000, 36, 4.75)
print(myLoan.calculate_monthly_payment())
print((f"Total amount paid: {myLoan.calculate_total_amount_paid()} "))

#leap validation
def check_leap_year(year):
    """Check if a year is leap or not"""
    if  (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print (f"{year} is a Leap Year.")
        return False
    else:
        print (f"{year} is Not a Leap Year.")
        return True
    
currentYear=int(input('Enter current Year: '))
check_leap_year(currentYear)
print(check_leap_year)
    
#loan calculation with leap year adjustment
if check_leap_year==False:
    myLeapLoan=LoanCalculator(10000+(1000*9/12),36+9,4.75/4)
else:
    myLeapLoan=LoanCalculator(10000,36,4.75)
    print(myLeapLoan.calculate_monthly_payment())
    print("Monthly Payment in non-leap year: ",myLoan.calculate_monthly_payment())
    
print("Without Adjustment:\n",myLeapLoan.calculate_monthly_payment(),"\nTotal Amount Paid: ",myLeapLoan.calculate_total_amount_paid())
print("The loan details in non-leap year are as follows:\n")
print(myLeapLoan.__dict__)
print("\n\nThe loan details in",currentYear,"are as follows:\n")
print(myLeapLoan.__dict__)
    





    








    

