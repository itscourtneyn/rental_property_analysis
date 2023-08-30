# Define the class
class RentalPropertyAnalysis():
    
    def __init__(self):
        self.total_monthly_income = 0
        self.total_monthly_expenses = 0
        self.annual_cash_flow = 0
# Define the terms and actions

#calculate the total monthly income
    def monthlyIncome(self):
        monthly_income= []
        rental_income = int(input("What is the total monthly rental income? "))
        monthly_income.append(rental_income)
        laundry_income = int(input("What is the total monthly laundry income? "))
        monthly_income.append(laundry_income)
        storage_income = int(input("What is the total monthly storage income? "))
        monthly_income.append(storage_income)
        misc_income = int(input("What is the total remaining monthly income from miscellaneous sources? "))
        monthly_income.append(misc_income)
        self.total_monthly_income = sum(monthly_income)
        print(f"The total monthly income for this property is ${self.total_monthly_income}.")

#calculate the total monthly expenses
    def monthlyExpenses(self):
        monthly_expenses=[]
        utilities_cost=[]
        taxes = int(input("How much are taxes per month? "))
        monthly_expenses.append(taxes)
        insurance = int(input("How much is insurance per month? "))
        monthly_expenses.append(insurance)
        water = int(input("How much is the monthly water cost to landlord? If tenant paid, enter 0. "))
        utilities_cost.append(water)
        sewer = int(input("How much is the monthly sewer cost to landlord? If tenant paid, enter 0. "))
        utilities_cost.append(sewer)
        garbage = int(input("How much is the monthly garbage removal cost to landlord? If tenant paid, enter 0. "))
        utilities_cost.append(garbage)
        electric = int(input ("How much is the monthly electric cost to landlord? If tenant paid, enter 0. "))
        utilities_cost.append(electric)
        gas = int(input("How much is the monthly gas cost to landlord? If tenant paid, enter 0. "))
        utilities_cost.append(gas)
        utilities = sum(utilities_cost)
        monthly_expenses.append(utilities)
        hoa_fees = int(input("How much are HOA fees monthly? "))
        monthly_expenses.append(hoa_fees)
        lawn_snow = int(input("What is the monthly cost of lawn and snow care for the landlord? If tenant handles, enter 0. "))
        monthly_expenses.append(lawn_snow)
        vacancy = int(input("How much will you be allocating to vacancy budget monthly? "))
        monthly_expenses.append(vacancy)
        repairs = int(input("How much will you be allocating to repairs budget monthly? "))
        monthly_expenses.append(repairs)
        cap_ex = int(input("How much will you be allocating to capital expeditures budget monthly? "))
        monthly_expenses.append(cap_ex)
        pm = int(input("What is the monthly property management expense?  If self-managed, enter 0. "))
        monthly_expenses.append(pm)
        mortgage = int(input("What is the monthly mortgage payment amount? "))
        monthly_expenses.append(mortgage)
        self.total_monthly_expenses = sum(monthly_expenses)
        print(f"The total monthly expense for this property is ${self.total_monthly_expenses}.")

# Calculate the monthly and annual cash flow
    def cashFlow(self):
        total_monthly_cash_flow = self.total_monthly_income - self.total_monthly_expenses
        self.annual_cash_flow = total_monthly_cash_flow * 12 
        print(f"The total monthly cash flow for this property is ${total_monthly_cash_flow} which makes the total annual cash flow ${self.annual_cash_flow}.")

# Calculate the Cash on Cash Return on Investment (ROI)
    def cashOnCashROI(self):
        total_invested = []
        down_payment = int(input("How much was the down payment? "))
        total_invested.append(down_payment)
        closing_costs = int(input("What was the total amount of closing costs? "))
        total_invested.append(closing_costs)
        rehab_costs = int(input("What was the total cost of rehab/repairs? If none, enter 0. "))
        total_invested.append(rehab_costs)
        self.total_investment = sum(total_invested)
        print(f"The total investment for this property is {self.total_investment}")
        coc_roi = (self.annual_cash_flow / self.total_investment) * 100
        print(f"The Cash on Cash ROI for this property is {coc_roi:.2f}%.")


def run():
    while True: 
        analysis = RentalPropertyAnalysis() 
        response = input("Let's begin the rental property analysis.  \nPlease enter all responses as numbers only, no '$' or decimals needed. \nEnter 'quit' at any time to quit the program. \nEnter 'begin' when you are ready. ")
        if response.lower() == 'quit':
            break
        else:
            analysis.monthlyIncome()
            analysis.monthlyExpenses()
            analysis.cashFlow()
            analysis.cashOnCashROI()
            break
run()
