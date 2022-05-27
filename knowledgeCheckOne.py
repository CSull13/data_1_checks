#a statement that prints "Hello World"
print('Hello World!')

#a list of several items, print one item from list. I decided to use some of my all time favorite movies
favoriteMovies = ['Mandy', 'Cloud Atlas', 'Swiss Army Man']
print(favoriteMovies[0])

#a dictioary populated with at least 2 keys and 2 values, print one. I decided to use my World of Warcraft character's
#gear, which stores the current equipped gear values and returns the item level of the corresponding slot, as requested by user
gearItemLevel = {
    "helmet" : 291,
    "neck" : 278,
    "back" : 278,
    "shoulders" : 272,
    "chest" : 278,
    "bracers" : 272, 
    "mainHand" : 278,
    "offHand" : 278,
    "gloves" : 278,
    "belt" : 278,
    "legs" : 278,
    "boots" : 262,
    "ringOne" : 291,
    "ringTwo" : 272,
    "trinketOne" : 272,
    "trinketTwo" : 262
}
currentGear = ""
while True:
    currentGear = input ("Enter a piece of gear or END to end: ")
    if currentGear == "END":
        print ("Have a nice day! ")
        break
    if currentGear not in gearItemLevel:
        print("Invalid entry, please enter a gear slot ")
    else:
        print(gearItemLevel[currentGear]) 