print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_bill = float(input("How many people to split the bill? "))

total_and_tip = (total_bill * (percentage_tip/100)) + total_bill
final = total_and_tip / split_bill
final = round(final, 2)
final_amount = "{:.2f}".format(final)

print(f"Each person should pay: ${final_amount}")