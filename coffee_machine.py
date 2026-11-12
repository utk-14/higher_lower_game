
from data import resources_required
from data import resources_availabel
def item_calc(item):
     x = resources_required[item]["Water"]
     y = resources_required[item]["Milk"]
     w = resources_required[item]["Coffee"]

     p = resources_availabel["Water"]
     q = resources_availabel["Milk"]
     r = resources_availabel["Coffee"]

     if p>=x and q>=y and r>=w:
          print(f"We have sufficient resources please proceed for coins insertion")
          coin_calc(item)
     else:
          print("insufficent resources")
          
def coin_calc(item):
     x = float(input("Enter quarters you are going to pay: "))
     y = float(input("Enter dimes you are going to pay: "))
     z = float(input("Enter nickeles you are going to pay: "))
     w = float(input("Enter pennies you are going to pay: "))

     total = x*0.25+y*0.1+z*0.05+w*0.01
     print(f"Money you paid {total}")
     p = resources_required[item]["Money"]
     resources_availabel["Money"]+=total
     resources_availabel["Milk"]-=resources_required[item]["Milk"]
     resources_availabel["Water"]-=resources_required[item]["Water"]
     resources_availabel["Coffee"]-=resources_required[item]["Coffee"]
     if p<=total:
          print(f"Enjoy your {item}")
          print(resources_availabel)

          if total>p:
               print(f"coin change: {total-p}")
     else:
          print("Insufficient resources,money refunded sucessfully")


flag = True
while(flag):

     choice = input("What would you like? espresso/latte/cappuccino").title()

     #If owner want to off it 
     if choice == "Off":
          flag = False
     elif choice=="Report":
          print(resources_availabel)
     elif choice=="Espresso":
          item_calc("Espresso")
     elif choice=="Latte":
          item_calc("Latte")       
     elif choice=="Cappuccino":
          item_calc("Cappuccino") 
     else :
          print("No such product available please choose valid product")               
