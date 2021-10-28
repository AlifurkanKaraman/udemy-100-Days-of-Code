print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_to_split = int(input("How many people to split the bill? "))

total_with_percentage = total_bill + total_bill * (percentage_tip / 100)
people_should_pay = total_with_percentage / people_to_split
print('Each person should pay: $' + "{:.2f}".format(people_should_pay))