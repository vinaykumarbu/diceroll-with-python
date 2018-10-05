import random
def func_roll(dec):
		num = random.randint(1,6)
		print(num)
		B = raw_input("Do you want to roll again?Enter 'roll': ")
		if B == "roll":
			func_roll(B)
 
dec = raw_input("Do you want to roll the dice? Enter 'roll': ")
func_roll(dec)