import random 
moves=["rock","paper","scissor"]


player=input("enter your move:").lower()
computer=random.choice((moves))
print("player:",player)
print("computer:",computer)
if player==computer:
       print("Result: DRAW")
elif (player=="rock" and computer=="scissor")or \
     (player=="paper" and computer=="rock")or \
     (player=="scissor" and computer=="paper"):
      print("Result: YOU WIN")
else:
    print("Result: YOU LOSE")
