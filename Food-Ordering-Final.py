print("WELCOME TO ZAB'S DINER")
youBuy = []
yourPrice = []
yourQuantity = []
dine = input("Would you like to dine with us?[Y/N]:")
if (dine.upper()=="Y"):
    foods = ["Deluxe Burger","Chilidog","Sandwich","Hotdog","Chicken"]
    foodPrice = [95,85,80,60,87];
    foodStocks = [1000,770,875,890,900];
    drinks = ["Mango","Juice","Milk","Beer","Soda"]
    drinkPrice = [20,15,15,35,15]
    drinkStocks = [1000,1000,1000,1000,1000]
    buy = True
    while(buy):      
        dine1 = input("Would you to order Lunch or Drinks?[L/D]:")
        if dine1.upper()=="L":
            print("\n\nMENU")
            o = 1
            print("FOODS\t\t\tPRICE\t\tSTOCKS")
            for i in foods:
                print("[" +str(o) + "] " + i,end="" )
                if o!=1:
                    print("\t\t",end="")
                else:
                    print("\t",end="")
                print(str(foodPrice[o-1]) +"\t\t" + str(foodStocks[o-1]))
                o = o+1
            choice = 0
            while choice<1 or choice>5:
                choice = int(input("Enter choice: "))
            quantity = int(input("Enter quantity:"))
            if(quantity>foodStocks[choice-1]):
                print("Your quantity is not enough stocks!")
            else:
                youBuy.append(foods[choice-1])
                yourPrice.append(foodPrice[choice-1])
                yourQuantity.append(quantity)
                foodStocks[choice-1] = foodStocks[choice-1] - quantity        
            choice = input("Buy again [Y/N]:")
            if (choice.upper()=="Y"):
                buy = True
            elif (choice.upper() =="N"):
                buy = False
            else:
                break
        elif dine1.upper()=="D":
            o = 1
            print("DRINKS\t\t\tPRICE\t\tSTOCKS")
            for i in drinks:
                print("[" +str(o) + "] " + i +"\t\t" + str(drinkPrice[o-1]) + "\t\t" +str(drinkStocks[o-1]))
                o = o+1
            choice = 0
            while choice<1 or choice>5:
                choice = int(input("Enter choice: "))
            quantity = int(input("Enter quantity:"))
            if(quantity>drinkStocks[choice-1]):
                print("Your quantity is not enough stocks!")
            else:
                youBuy.append(drinks[choice-1])
                yourPrice.append(drinkPrice[choice-1])
                yourQuantity.append(quantity)
                drinkStocks[choice-1] = drinkStocks[choice-1] - quantity
            choice = input("Buy again [Y/N]:")
            if (choice.upper()=="Y"):
                buy = True
            elif (choice.upper() =="N"):
                buy = False
            else:
                break
    print("-"*80)
    print("\t\t\t------RECEIPT------")
    check = 0;
    total = 0
    print("-"*80)
    print("Item:\t\t\tPrice:\t\tQuantity:\t\t Amount:")
    print("-"*80)
    for i in youBuy:
        print(youBuy[check] +"\t\t\t"+str(yourPrice[check]) + "\t\t\t " +str(yourQuantity[check])+"\t\t "+ str(yourPrice[check] * yourQuantity[check]))
        total = total + (yourPrice[check] * yourQuantity[check])
        check = check + 1    
    print("-"*80)    	
    print("Total:" + str(total))
    print("-"*80)
    print("\n\nTHANKYOU!!!")
elif (dine.upper()=="N"):
    print("Have a nice day!")