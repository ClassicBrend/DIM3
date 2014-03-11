from random import randint

def determineOutcome(food,ammo,zombies,surv):
    while zombies > 0:
        if player.ammo > 0:
            zombies -= 1
            player.ammo -= 1
        else:
            player.survivors -= 1
            zombies -= 1
    player.ammo += ammo
    player.food += food
    player.survivors += surv
    player.moves -= 1

def newarea():
	global houses
	houses=[]
	house1=House()
	houses.append(house1)
	house2=House()
	houses.append(house2)
	house3=House()
	houses.append(house3)
	house4=House()
	houses.append(house4)
	house5=House()
	houses.append(house5)	

def test():
	testText = "test"
	return testText
	
	
	
def rummage(houseNum):
	if player.moves > 0:
		house=houses[houseChoice]
		room = dict[houseNum]
	
		print "player enters house ", houseNum, " which has ", house.roomsInHouse, " rooms"
		print "survivors: ", player.survivors
		print "food: ", player.food
		print "ammo: ", player.ammo
		print "zomb: ", house.zombiesInHouse
		print "ROOM = ", room, " HOUSE = ", houseNum
		determineOutcome(house.foodInHouse[room],house.ammoInHouse[room],house.zombiesInHouse[room],house.survivorsInHouse[room])
	
		print "player leaves room ", room + 1, " with"
		print "survivors: ", player.survivors
		print "food: ", player.food
		print "ammo: ", player.ammo
		print "moves left: ", player.moves
		print "---------------------------------"
		room += 1
		dict[houseNum] = room
	else:
		print "No more moves"
	
class House():

	def __init__(self):
	    self.roomsInHouse = randint(1,3)
	    self.foodInHouse = []
	    self.ammoInHouse = []
	    self.zombiesInHouse = []
	    self.survivorsInHouse = []
	    
	    for i in range(0,self.roomsInHouse):
			self.foodInHouse.append(randint(1,10))
			self.ammoInHouse.append(randint(0,10))
			self.zombiesInHouse.append(randint(0,5))
			self.survivorsInHouse.append(randint(0,3))

class Player():

	def __init__(self):
	    self.survivors=3
	    self.food = 0
	    self.ammo = 0
	    self.moves = 8


def startGame():
	player = Player()
	newarea()
	houseChoice = 0
	dict = {0:0,1: 0, 2: 0, 3: 0, 4: 0};
	return player.survivors
#	print "|||||||||||||||||||"
#	print "| House Generator |"
#	print "|||||||||||||||||||"
#	print ""
#	print "player stats"
#	print "survivors: ", player.survivors
#	print "food: ", player.food
#	print "ammo", player.ammo
#	print "moves: ", player.moves
#	print ""
#	print "There are ", len(houses), " houses"
#	print ""

#	while player.survivors>0:
#		if player.moves < 8:
#			a=raw_input("Would you like to move to another house y/n:")
#			if a=="n":
#				if house.roomsInHouse == dict[houseChoice]:
#					print "The house is empty, pick another!"
#				else:
#					rummage(houseChoice)
#					continue
#			else:
#				player.moves -= 1
#
#
#		if houseChoice != 0:
#			previousChoice = houseChoice
#		else:
#			previousChoice = houseChoice
#		if player.moves > 0:
#			houseChoice = input("Pick a house: ")
#			house = houses[houseChoice]
#			if house.roomsInHouse == dict[houseChoice]:
#				print "The house is empty, pick another!"
#			else:
#				rummage(houseChoice)
#			
#	print "GAME OVER"

