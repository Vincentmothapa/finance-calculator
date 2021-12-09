import math

# Display initial message.
print("Choose either 'investments' or 'bond' from the menu below to \
proceed:\n")

print("investment   - to calculate the amount of interest you'll earn \
on interest")

print("bond         - to calculate the amount you'll have to pay on a \
home loan\n")

# Get user choice between investment and bond, and make it lowercase.
choice = input("Enter your choice: ").lower()


#========================================================================
# IF INVESTMENT IS CHOSEN.
if choice == 'investment':
    amount = float(input("\nEnter the amount you are depositing: "))
    rate = float(input("Enter the interest rate as a percentage: "))
    years = float(input("How many years do you plan on investing? "))
    print("\nDo you want simple or compound interest?")
# Get interest type and make it lowercase.
    interest_type = input("Only enter 'simple' or 'compound': ").lower()
    
# Choose interest type, simple or compound.
# Simple interest
    if interest_type == 'simple':
        investment_value = round(amount*(1 + (rate/100)*years), 2)
        print(f"\nYou will get R{investment_value} after {years} years.")

# Compound interest
    else:
        investment_value = round(amount*math.pow(1+rate/100, years), 2)
        print(f"\nYou will get R{investment_value} after {years} years.")


#========================================================================
# IF BOND IS CHOSEN.
elif choice == 'bond':
    p_value = float(input("\nEnter the present value of the house: "))
    rate = float(input("Enter the interest rate as a percentage: "))
    monthly_rate = rate/1200
    months = float(input("How many months do you plan to take to repay \
the bond? "))

# Formula for bond repayment.
    repayment=(monthly_rate*p_value)/(1-math.pow(1+monthly_rate,-months))
# Round of repayment to 2 decimal places.
    rounded = round(repayment, 2)
    print(f"\nYou will pay R{rounded} monthly for {months} months.")


#========================================================================
# Error message for incorrect entry.
else:
    print("Incorrect entry. Please enter either 'investment' or 'bond'.")












