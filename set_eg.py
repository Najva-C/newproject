usera={"spiderman","ironman","superman","batman"}
userb={"ironman","batman","thor","captain america"}
common=usera & userb
print("Movies that both of them watched:",common)
unique=usera - userb
print("movies that user A watched:",unique)
recommend=userb - usera
print("movies suggetion of user A to user B:",recommend)
