print("Electricity bill estimator 2.0", '\n')

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = int(input("Which tariff? 11 or 31: "))
while not (tariff == 11 or tariff == 31):
    print("Invalid number!")
    tariff = int(input("Which tariff? 11 or 31: "))

if tariff == 11:
    price = TARIFF_11
else:
    price = TARIFF_31

use = float(input("Enter daily use in kWh: "))
bill_days = int(input("Enter number of billing days: "))
total = price * use * bill_days
print()
print("Estimated bill: ${:.2f}".format(total))