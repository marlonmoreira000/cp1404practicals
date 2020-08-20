print("Electricity bill estimator 2.0")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = int(input("Which tariff? 11 or 31: "))

if tariff == 11:
    cents_per_kilowatt_hr = TARIFF_11 * 100
    daily_kilowatt_usage = float(input("Enter daily use in kWh: "))
    number_of_billing_days = int(input("Enter number of billing days: "))
    estimated_bill = (cents_per_kilowatt_hr / 100) * daily_kilowatt_usage * number_of_billing_days
    print("Estimated bill: $", estimated_bill)
elif tariff == 31:
    cents_per_kilowatt_hr = TARIFF_31 * 100
    daily_kilowatt_usage = float(input("Enter daily use in kWh: "))
    number_of_billing_days = int(input("Enter number of billing days: "))
    estimated_bill = (cents_per_kilowatt_hr / 100) * daily_kilowatt_usage * number_of_billing_days
    print("Estimated bill: $", estimated_bill)
else:
    print("Invalid input")