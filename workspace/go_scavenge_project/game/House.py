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
				self.ammo -= randint(1,2)
				self.survivors -= randint(0,1)
			else:
				self.survivors -= 1
				
				zombies -= 1

	def pickleData(self):
		dic={"moves":self.moves,"food":self.food,"ammo":self.ammo,"survivours":self.survivors,"atHouse":self.atHouse,"dayno":self.dayno,"houses":self.houses}
		pickle.dump( dic, open( "save.p", "wb" ) )
		pass

	def unpickleData(self):
		dic= pickle.load( open( "save.p", "rb" ) )
		updateData(self,dic["moves"],dic["food"],dic["ammo"],dic["survivours"],dic["atHouse"],dic["dayno"],dic["houses"])
		self.houses=dic["houses"]
		
	def updateData(self, curMoves, curFood, curAmmo, curSurvivors, curHouse, curDay):
		self.moves = curMoves
		self.food = curFood
		self.ammo = curAmmo
		self.dayno = curDay
		self.survivors = curSurvivors
		if curHouse != self.athouse:
			self.moves -= 1
		if curMoves <= 1:
			self.dayno += 1
			self.moves = 9


	def report(self):
		rep = []
		rep.append(self.survivors)
		rep.append(self.food)
		rep.append(self.ammo)
		rep.append(self.moves)
		rep.append(self.athouse)
		rep.append(self.dayno)
		return rep

