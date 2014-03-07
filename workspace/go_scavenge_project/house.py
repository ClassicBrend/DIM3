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

	def __init__(self,s):
	    self.survivors=s
	    self.food = 0
	    self.ammo = 0

player = Player(4)

newarea()
print "|||||||||||||||||||"
print "| House Generator |"
print "|||||||||||||||||||"
print ""
print "player stats"
print "survivors: ", player.survivors
print "food: ", player.food
print "ammo", player.ammo
print ""
print "There are ", len(houses), " houses"
print ""


while player.survivors>0:
	a=raw_input("Would you like to move to a new area y/n:")
	if a=="y":
		newarea()
		i =input("Pick a house: ")
		
		

		print "player enters house ",i,
		print "survivors: ", player.survivors
		print "food: ", player.food
		print "ammo: ", player.ammo
		print ""
		
		house=houses[i]
		for j in range(0,house.roomsInHouse):
			print "food: ", house.foodInHouse[j]
			print "ammo: ", house.ammoInHouse[j]
			print "zomb: ", house.zombiesInHouse[j]
			print "surv: ", house.survivorsInHouse[j]
			print ""
			print ""
			determineOutcome(house.foodInHouse[j],house.ammoInHouse[j],house.zombiesInHouse[j],house.survivorsInHouse[j])
			print "player leaves room ",j," with "
			print "survivors: ", player.survivors
			print "food: ", player.food
			print "ammo: ", player.ammo
			print "---------------------------------"
	elif a=="n":
		i =input("Pick a house: ")
		
		

		print "player enters house ",i,
		print "survivors: ", player.survivors
		print "food: ", player.food
		print "ammo: ", player.ammo
		print ""
		
		house=houses[i]
		for j in range(0,house.roomsInHouse):
			print "food: ", house.foodInHouse[j]
			print "ammo: ", house.ammoInHouse[j]
			print "zomb: ", house.zombiesInHouse[j]
			print "surv: ", house.survivorsInHouse[j]
			print ""
			print ""
			determineOutcome(house.foodInHouse[j],house.ammoInHouse[j],house.zombiesInHouse[j],house.survivorsInHouse[j])
			print "player leaves room ",j," with "
			print "survivors: ", player.survivors
			print "food: ", player.food
			print "ammo: ", player.ammo
			print "---------------------------------"
