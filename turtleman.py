###Def###

def hunger_death():
	print "You died of hunger..."
	print "Items Traded: ", give1, ",", give2, ",", give3
	print "Land Walked: ", land
	turtle.up()
	life = "false"
	while 1==1:
		turtle.color("Red")

def trade_ai_1():
	b = random.randint(1,3)
	if b == 1:
		item1 = "Nothing"
	elif b == 2:
		item1 = "Wheat"
	elif b == 3:
		item1 = "Fur"

###Main Code###

import turtle
turtle.forward(0)
life = "true"
land = 0
give1 = "Nothing"
give2 = "Nothing"
give3 = "Nothing"
cash = 0
hunger = 100
while life == "true":
	import random
	a = random.randint(1,5)
	if a == 1:
		turtle.forward(5)
		hunger = hunger - 1
		land = land + 1
		if hunger < 1:
			hunger_death()
	elif a == 2:
		turtle.forward(5)
		hunger = hunger - 1
		land = land + 1
		if hunger < 1:
			hunger_death()
	elif a == 3:
		turtle.left(45)
		land = land + 1
	elif a == 4:
		turtle.right(45)
		land = land + 1
	elif a == 5:
		a = random.randint(1,5)
		if a == 1:
			print "You found food!"
			hunger = hunger+10

### ITEM ID ###
		a = random.randint(1,20)
		if a == 1:
			a = random.randint(1,8)
			if a == 1:
				item1 = "Nothing"
			elif a == 2:
				item1 = "Wheat"
			elif a == 3:
				item1 = "Wheat"
			elif a == 4:
				item1 = "Wheat"
			elif a == 5:
				item1 = "Fur"
			elif a == 6:
				item1 = "Fur"
			elif a == 7:
				item1 = "Silver"
			elif a == 8:
				item1 = "Silver"

			b = random.randint(1,8)
			if b == 1:
				item2 = "Wheat"
				while item1 == item2:
					trade_ai_1()
			elif b == 2:
				item2 = "Wheat"
				while item1 == item2:
					trade_ai_1()
			elif b == 3:
				item2 = "Wheat"
				while item1 == item2:
					trade_ai_1()
			elif b == 4:
				item2 = "Fur"
				while item1 == item2:
					trade_ai_1()
			elif b == 5:
				item2 = "Fur"
				while item1 == item2:
					trade_ai_1()
			elif b == 6:
				item2 = "Silver"
				while item1 == item2:
					trade_ai_1()
			elif b == 7:
				if item1 == "Nothing":
					item2 = "Food"
				item2 = "Gold"
			elif b == 8:
				item2 = "Food"
				while item1 == item2:
					trade_ai_1()

### TRADE ###
			print "You found a village!"
			print "Villager wants ", item1, " for ", item2
			print "Would you like to trade?"
			yesno = raw_input("y/n: ")
			if yesno == "y":
				print "Select the item from your inventory:"
				print "1) ", give1
				print "2) ", give2
				print "3) ", give3
				trading = raw_input("Item Slot #:")
				if trading == "1":
					if give1 == item1:
						give1 = item2
						print "Trade successful!"
						if give1 == "Food":
							hunger = hunger + 30
							give1 = "Nothing"
						elif give1 == "Gold":
							if give2 == "Gold":
								if give3 == "Gold":
									print "You win!"
									print "Items Traded: ", give1, ",", give2, ",", give3
					elif give1 != item1:
						print "Invalid trade option."
						hunger = hunger + 20
				elif trading == "2":
					if give2 == item1:
						give2 = item2
						print "Trade successful!"
						if give2 == "Food":
							hunger = hunger + 30
							give2 = "Nothing"
						elif give1 == "Gold":
							if give2 == "Gold":
								if give3 == "Gold":
									print "You win!"
									print "Items Traded: ", give1, ",", give2, ",", give3
					elif give3 != item2:
						print "Invalid trade option."
						hunger = hunger + 20
				elif trading == "3":
					if give3 == item1:
						give3 = item2
						print "Trade successful!"
						if give3 == "Food":
							hunger = hunger + 30
							give3 = "Nothing"
						elif give1 == "Gold":
							if give2 == "Gold":
								if give3 == "Gold":
									print "You win!"
									print "Items Traded: ", give1, ",", give2, ",", give3
					elif give3 != item1:
						print "Invalid trade option."
						hunger = hunger + 20
				else:
					print "Invalid trade option."
			if yesno == "n":
				print "Trade is canceled."
