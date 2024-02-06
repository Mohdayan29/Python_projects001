############# TIP CALCULATOR ############
#welcome to the tip calculator
print("Welcome to the tip calculator :)")

#what is the total bill
print("what is the total bill?")
num_1 = int(input())

#what percentage tip would you like to give
print("what percentage tip would you like to give 10,12,or 15?")
num_2 =int(input())
tip = num_1*(num_2/100)
amount_after_tip = num_1+tip
print(amount_after_tip)

#How many people to split the bill
print("no of peoples?")
num_3 = int(input())
Tip_calculated = amount_after_tip/num_3

#Each person should pay
print(Tip_calculated)


