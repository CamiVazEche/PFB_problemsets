#!/usr/bin/env python3
import sys
print ("My name: Camila")
print ("occupation: postdoc")
print ("favorite color: green")

fav_act = "listening to music" #defines favorite activity
print ("favorite activity:" , fav_act)

fav_food = "pizza" #defines favorite food
print (f"favorite food: {fav_food}")

fav_animal = "elephant" #defines favorite animal
print ("favorite animal:" , fav_animal)

fav_act = sys.argv[1]
fav_food = sys.argv[2]
fav_animal = sys.argv[3]
print('Favorite activity:', fav_act, 'Favorite food:', fav_food, 'Favorite animal:', fav_animal)
