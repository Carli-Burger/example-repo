import math
# Start with printing an introduction  where the user gets a definition of investment and bond.
# User must be able to choose between investment or bond.
print('''Investement - to calculate the amount of interest you'll earn on your investment.
    Bond - to calculate the amount you'll have to pay on a home load.''')
user_entry = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).strip().lower()
# If user input is investment, the user will be asked their deposit, interest rate, period.

if user_entry == "investment":
    invest_deposit = float(input("Please enter amount you want to deposit: "))
    invest_interest_rate = int(input("Enter the interest rate: "))/100
    invest_period = int(input("Number of years you plan on investing: "))
    invest_interest = str(input("Do you want 'simple' or 'compound' interest? "))
# User will be asked to make a choice between simple or compund interest.
# Depending on the interest type the user inputs a calculation will follow.
    if invest_interest == "simple":
        simple_interest_calc = invest_deposit * (1 + (invest_interest_rate)*invest_period)
        print("Amount at Simple Interest: ", simple_interest_calc)
    elif invest_interest == "compound":
        compound_interest_calc = invest_deposit * math.pow(1 + (invest_interest_rate), invest_period)
        print("Amount at Compound Interest: ", compound_interest_calc)
    else: print("Invalid input entered")
# If user input is bond, they will be prompted to input their present value of their hou, interest rate and peiod.
# Bond monthly payment will be calculated once user input all the requested information.
elif user_entry == "bond":
    bond_present_value = float(input("Please enter the present value of your house: "))
    bond_interest_rate = int(input("Enter the interest rate: "))/100/12
    bond_period = int(input("Number of months you plan to repay the bond: "))
    bond_repayment = ((bond_interest_rate) * bond_present_value)/(1 - (1 + (bond_interest_rate))**( - bond_period))
    print("Your monthly repayment: " , bond_repayment)

else:
    print("Please choose a valid option: Investment or Bond.")
