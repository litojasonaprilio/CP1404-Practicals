print("Electricity bill estimator", '\n')

price = int(input("Enter cents per kWh: "))
use = float(input("Enter daily use in kWh: "))
bill_days = int(input("Enter number of billing days: "))
total = (0.01*price) * use * bill_days
print()
print("Estimated bill: ${:.2f}".format(total))