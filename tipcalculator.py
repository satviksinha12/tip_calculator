print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
final_bill= tip/100 * bill + bill
bill_per_person = final_bill/people
print("Total bill to be paid along with tip",final_bill)
print("Each person should pay:",bill_per_person)
