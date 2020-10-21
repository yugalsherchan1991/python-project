#%%
balance = 42
interestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterest = interestRate/12
for i in range(12):
    monthlyPayment = monthlyPaymentRate *balance
    monthlyUnpaidBal = balance - monthlyPayment
    balance = round(monthlyUnpaidBal + (monthlyInterest * monthlyUnpaidBal),2)
    print ( "Month " + str(i + 1) + " remaining balane is : " + str(balance))

    
 # %%
def balanceRecur(balance, InterestRate, monthlyPaymentRate, numberOfPayments):
    if numberOfPayments == 0:
        return balance
    return balanceRecur(balance*(1-monthlyPaymentRate) * (1+(InterestRate/12)), InterestRate, monthlyPaymentRate, numberOfPayments-1)
print('Remaining balance: ' + str(round(balanceRecur(484, 0.2, 0.04, 12), 2)))


# %%
'''
This is a code snippet which calculate minmunm monthly payment required 
to pay off the credit card with compunding interest everymonth.
'''

balance = 3926
monthlyInterest = (0.2/12)
minMonthlyPayment = 10
newBalance = balance
while newBalance >= 0 :
    minMonthlyPayment = minMonthlyPayment + 10
    newBalance = balance 
    for i in range (1,13):
        
        monthlyUnpaidBal = newBalance - minMonthlyPayment
        newBalance = monthlyUnpaidBal + ( monthlyInterest * monthlyUnpaidBal)
    
print( minMonthlyPayment)


# %%

'''
Calulate minimum monthly payment with bisection method 
'''
monthlyInterest = 0.2/12
balance = 320000
monthlyLowerBound = round(balance/12,2)
monthlyUpperBound = round((balance * (1 +monthlyInterest)**12)/12,2)
guess = (monthlyUpperBound + monthlyLowerBound)/2


# %%
