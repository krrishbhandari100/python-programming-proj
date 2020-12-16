import random
print("s for snake")
print("w for water")
print("g for gun")
times = int(input("How many times you want to play: "))
possibleOutcomes = ["s", "w", "g"]
computerPoints = 0
userPoints = 0
for i in range(0, times):
    user_inp = input("Enter your choice: ")
    BOT = random.choice(possibleOutcomes)
    # case 1 s as user
    if(user_inp=="s" and BOT=="s"):
        print("*******************************************************************************")
        print("tie")
        print("You choosed", user_inp)
        print("Computer choosed", BOT)
        userPoints = userPoints + 0
        computerPoints = computerPoints + 0
        print("The Computer Point is: ", computerPoints)
        print("The User Point is: ", userPoints)
        print("*******************************************************************************")
    
    elif(user_inp=="s" and BOT=="w"):
        print("*******************************************************************************")
        print("You win")
        print("You choosed", user_inp)
        print("Computer choosed", BOT)
        userPoints = userPoints + 1
        computerPoints = computerPoints + 0
        print("The Computer Point is: ", computerPoints)
        print("The User Point is: ", userPoints)
        print("*******************************************************************************")
    
    elif(user_inp=="s" and BOT=="g"):
        print("*******************************************************************************")
        print("You loose")
        print("You choosed", user_inp)
        print("Computer choosed", BOT)
        userPoints = userPoints + 0
        computerPoints = computerPoints + 1
        print("The Computer Point is: ", computerPoints)
        print("The User Point is: ", userPoints)
        print("*******************************************************************************")
    
    # case 2 w as user
    elif(user_inp=="w" and BOT=="s"):
        print("*******************************************************************************")
        print("You loose")
        print("You choosed", user_inp)
        print("Computer choosed", BOT)
        userPoints = userPoints + 0
        computerPoints = computerPoints + 1
        print("The Computer Point is: ", computerPoints)
        print("The User Point is: ", userPoints)
        print("*******************************************************************************")
    
    elif(user_inp=="w" and BOT=="w"):
        print("*******************************************************************************")
        print("You tie")
        print("You choosed", user_inp)
        print("Computer choosed", BOT)
        userPoints = userPoints + 0
        computerPoints = computerPoints + 0
        print("The Computer Point is: ", computerPoints)
        print("The User Point is: ", userPoints)
        print("*******************************************************************************")
    
    elif(user_inp=="w" and BOT=="g"):
        print("*******************************************************************************")
        print("You win")
        print("You choosed", user_inp)
        print("Computer choosed", BOT)
        userPoints = userPoints + 1
        computerPoints = computerPoints + 0
        print("The Computer Point is: ", computerPoints)
        print("The User Point is: ", userPoints)
        print("*******************************************************************************")

    # case 3 g as user
    elif(user_inp=="g" and BOT=="s"):
        print("*******************************************************************************")
        print("You won")
        print("You choosed", user_inp)
        print("Computer choosed", BOT)
        userPoints = userPoints + 1
        computerPoints = computerPoints + 0
        print("The Computer Point is: ", computerPoints)
        print("The User Point is: ", userPoints)
        print("*******************************************************************************")
        
    
    elif(user_inp=="g" and BOT=="w"):
        print("*******************************************************************************")
        print("You loose")
        print("You choosed", user_inp)
        print("Computer choosed", BOT)
        userPoints = userPoints + 0
        computerPoints = computerPoints + 1
        print("The Computer Point is: ", computerPoints)
        print("The User Point is: ", userPoints)
        print("*******************************************************************************")
        
    
    elif(user_inp=="g" and BOT=="g"):
        print("*******************************************************************************")
        print("You tie")
        print("You choosed", user_inp)
        print("Computer choosed", BOT)
        userPoints = userPoints + 0
        computerPoints = computerPoints + 0
        print("The Computer Point is: ", computerPoints)
        print("The User Point is: ", userPoints)
        print("*******************************************************************************")


print("In final the computer point is: ", computerPoints)
print("In final the user point is: ", userPoints)
if(computerPoints > userPoints):
    print("you loose by", computerPoints - userPoints)
elif(computerPoints < userPoints):
    print("you won by", userPoints - computerPoints)
elif(computerPoints==userPoints):
    print("tie")
input()
# this input tag is for holding the screen when running from windows