import random
print("""Welcome to FLAPPY BIRDS
Instructions:
If the bird passes through the slot in the obstacles it shall get a point and if it fails to do so it will die, and the player will start fresh.
With pressing every enter the bird will move near the obstacles. 
Pressing W and then pressing enter key will push the bird up.
Pressing any other key and then pressing the enter key will push the bird down.""")
n=0
f=5
s=1
o=15
h=random.randrange(2,10)
while s==1:
    for i in range(1,f):
        if i==h:
            print(" "*30)
        else:
            print(" "*(o-1), "|", " "*(30-o))
    if f==h:
            print(" "*3, ":"," "*25)
    else:
        if o!=6:
            print(" "*3, ":"," "*(o-7), "|", " "*(30-o))
        else:
            print(" "*3, ":", "|", " "*(30-o))
        #  printing two strings side by side creates an extra space even if printed 0 or -ve times.
    for i in range(f+1,11):
        if i==h:
            print(" "*(o-1), " ", " "*(30-o))
        print(" "*(o-1), "|", " "*(30-o))
    x=input()
    if o==5 and h!=f:
        print("---Game Over---")
        print("Your score is: ",n)
        s=2
    elif o==5:
        h=random.randrange(2,10)
        o=15
        n=n+1
    if x=="w" or x=="W":
        f=f-1
#    elif x=="s"or x=="S":
#        f=f+1
    else:
        f=f+1
    o=o-1