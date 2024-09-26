import random
''''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,1,0])
youstr = input("enter the choice : ")
youdict = {"s":1, "w":-1, "g":0}
reverseddict = {1:"snake", -1 :"water", 0:"gun"}
you = youdict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"you choose {reverseddict[you]} and computer choose {reverseddict[computer]}")

if (computer == you):
    print("It's Draw")
else:

    ''''
    if(computer == -1 and you == 1 ):  #computer - you = -2
        print("you win")
    elif(computer == -1 and you == 0):  #computer - you = -1
        print("computer win")

    elif(computer == 1 and you == -1): #computer - you = 2
        print("you lose")
    elif(computer == 1 and you == 0): #computer - you = 1
        print("you win")

    elif(computer == 0 and you == -1): #computer - you = 1
        print("you lose")
    elif(computer == 0 and you == 1): #computer - you = -1
        print("you lose")

    the below logic is written on the basis of the values of computer - you

    '''

    if ((computer - you) == 0 or (computer -you) == -1):
        print("You lose!")
    else:
        print("You win!")
