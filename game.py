from random import choice
from string import ascii_uppercase
random=(''.join(choice(ascii_uppercase) for i in range(6)))
lis=list(random)
chances=0
while chances!=10 :
    user=input("Enter string in caps of length 6=")
    length=len(user)
    while length!=6:
        print("String length is not 6,Enter Another string of length=")
        user=input()
        length=len(user)
    userlis=list(user)
    same=0
    differ=0
    for i in range(6):
        if lis[i]==userlis[i]:
            same=same+1
        elif lis[i]==userlis[0] or lis[i]==userlis[1] or lis[i]==userlis[2] or lis[i]==userlis[3] or lis[i]==userlis[4] or lis[i]==userlis[5]:
            differ=differ+1
    if same==6:
        print ("Your Guess is correct")
        break
    else:
        print ("There are {} numbers in same position and {} numbers in different positions".format(same,differ))
        chances=chances+1
        print("you have {} chances left".format(10-chances))
if chances==10:
    print("You Failed to guess the string in 10 chances")
    print ("Answer is "+random)
