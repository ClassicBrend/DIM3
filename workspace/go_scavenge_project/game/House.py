from random import randint
import pickle

class House():

	def __init__(self):
		self.roomsInHouse = randint(1,5)
		self.foodInHouse = []
		self.ammoInHouse = []
		self.zombiesInHouse = []
		self.survivorsInHouse = []
		self.roomsExplored = 0
	    
		for i in range(0,self.roomsInHouse):
			self.foodInHouse.append(randint(1,10))
			self.ammoInHouse.append(randint(0,10))
			self.zombiesInHouse.append(randint(0,5))
			self.survivorsInHouse.append(randint(0,3))



	def inspectRoom(self):
		if self.roomsInHouse == self.roomsExplored:
			return (0,0,0,0)
		else:
			food = self.foodInHouse[self.roomsExplored]
			ammo = self.ammoInHouse[self.roomsExplored]
			zombies = self.zombiesInHouse[self.roomsExplored]
			survivors = self.survivorsInHouse[self.roomsExplored]
			self.roomsExplored += 1		
			return (food,ammo,zombies,survivors)
			

	def show_house(self):
		for i in range(0,self.roomsInHouse):
			print i, self.foodInHouse[i], self.ammoInHouse[i]



class Game():

	def __init__(self):
		self.survivors=3
		self.food = 0
		self.ammo = 0
		self.cost_move = 2
		self.cost_inspect = 1
		self.dayno = 0
		self.MAX_HOUSES = 5
		self.new_day()


	def generate_houses(self):
		self.houses = []
		for i in range(0,self.MAX_HOUSES):
			self.houses.append( House() )
		
	def new_day(self):
		self.moves = 8
		self.athouse = -1
		self.generate_houses()

	
	def selectHouse(self, houseno):
		if  houseno >=0 and houseno < self.MAX_HOUSES:
			self.athouse = houseno
			self.moves = self.moves - self.cost_move


	def inspectHouse(self):
		if self.athouse >= 0:
			self.moves = self.moves - self.cost_inspect
			fazs = self.houses[self.athouse].inspectRoom()

			self.food = self.food + fazs[0]
			self.ammo = self.ammo + fazs[1]
			self.survivors = self.survivors + fazs[3]
			self.handleZombies(fazs[2])
			
			
	def handleZombies(self, zombies):
		while zombies > 0:
			if self.ammo > 0:
				zombies -= 1
				self.ammo -= 1
			else:
				self.survivors -= 1
				zombies -= 1

	def pickleData(self):
		pass
		

#	def determineOutcome(food,ammo,zombies,surv):
#	    while zombies > 0:
#		if player.ammo > 0:
#		    zombies -= 1
#		    player.ammo -= 1
#		else:
#		    player.survivors -= 1
#		    zombies -= 1
#	    player.ammo += ammo
#	    player.food += food
#	    player.survivors += surv
#	    player.moves -= 1


	def report(self):
		print "player stats"
		print "survivors: ", self.survivors
		print "food: ", self.food
		print "ammo", self.ammo
		print "moves: ", self.moves
		print ""
		rep = []
		rep.append(self.survivors)
		rep.append(self.food)
		rep.append(self.ammo)
		rep.append(self.moves)
		return rep

	def gameOver(self):
		if(self.survivors<=0):
			print "Game Over"


#myhouse = House()
#myhouse.show_house()
#print myhouse.inspectRoom()
#print myhouse.inspectRoom()
#print myhouse.inspectRoom()
#print myhouse.inspectRoom()


mygame = Game()
mygame.report()
mygame.selectHouse(0)
mygame.report()
mygame.inspectHouse()
mygame.report()



