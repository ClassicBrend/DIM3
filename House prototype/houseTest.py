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
    
    
class House():
    roomsInHouse = randint(1,3)
    foodInHouse = []
    ammoInHouse = []
    zombiesInHouse = []
    survivorsInHouse = []
    for i in range(0,roomsInHouse):
        foodInHouse.append(randint(1,10))
        ammoInHouse.append(randint(0,10))
        zombiesInHouse.append(randint(0,5))
        survivorsInHouse.append(randint(0,3))
        
class Player():
    survivors = 3
    food = 0
    ammo = 0

    

house = House()
player = Player()


print "|||||||||||||||||||"
print "| House Generator |"
print "|||||||||||||||||||"
print ""
print "player stats"
print "survivors: ", player.survivors
print "food: ", player.food
print "ammo", player.ammo
print ""
print "There are ", house.roomsInHouse, " rooms in this house"
print ""

for i in range(0,house.roomsInHouse):
    print "player enters room ",i," with "
    print "survivors: ", player.survivors
    print "food: ", player.food
    print "ammo: ", player.ammo
    print ""

    print "Room number ", i
    print "food: ", house.foodInHouse[i]
    print "ammo: ", house.ammoInHouse[i]
    print "zomb: ", house.zombiesInHouse[i]
    print "surv: ", house.survivorsInHouse[i]
    print ""
    print ""
    determineOutcome(house.foodInHouse[i],house.ammoInHouse[i],house.zombiesInHouse[i],house.survivorsInHouse[i])
    print "player leaves room ",i," with "
    print "survivors: ", player.survivors
    print "food: ", player.food
    print "ammo: ", player.ammo
    print "---------------------------------"
    
    
    
