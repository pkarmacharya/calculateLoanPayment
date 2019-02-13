
remainingLoanBalance = input("What is your current loan balance? ")
interest = input("What percent is your fixed interest? ")
interest = interest/100.00
monthlyAmount = input("What will be you monthly loan payment? ")
years = input("How many years do you want to calculate?")

#print("Month 0: " + str(remainingLoanBalance))
months = (years * 12)+1
total = 0
for i in range (1, months):
    def myFunc(loanBalance):
        return lambda monthlyAmount, interest : loanBalance - (monthlyAmount-(loanBalance * interest)/12)

    paidInterest = remainingLoanBalance*interest/12
    total = total + paidInterest
    result = myFunc(remainingLoanBalance)
    remainingLoanBalance = result(monthlyAmount, interest)
    print("Month " + str(i) + ": " + str(remainingLoanBalance))
    #print("Interest Paid: " + str(paidInterest)+"\n")

print("Remaining Balance: " + str(remainingLoanBalance))
print("Total Interest Paid: " + str(total))
