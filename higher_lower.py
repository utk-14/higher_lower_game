import art
import random
from data import people
print(art.logo)

ct = 0

flag = True

while flag:
    
    x = random.randint(0,49)
    print(f"Compare A:{people[x]["name"]}, {people[x]["profession"]}, {people[x]["country"]}\n")
    print(f"{art.logo1}")
    y = random.randint(0,49)
    print(f"Against B:{people[y]["name"]}, {people[y]["profession"]}, {people[y]["country"]}\n")

    opinion = input("Who has more followers Type 'A' or 'B':")

    p = people[x]["followers"]
    q = people[y]["followers"]

    if p>q and opinion=="A":
        ct+=1
        print(f"you got it right current score {ct}")
        
    elif q>p and opinion=="B":
        ct+=1
        print(f"you got it right current score {ct}")
    elif p==q:
        ct+=1
        print(f"Both same but still you get one point {ct}")
    else:
        print("you lose!!!")
        print(f"Your score is {ct}")
        break

                 
