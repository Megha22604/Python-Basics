grocery_list=[]

while True:
    print("\n ------Grocery_List MENU------")
    print("\n 1] ➕ADD ITEM")
    print("\n 2] ❌DELETE ITEM")
    print("\n 3] 👁️VIEW LisT")
    print("\n 4] ✅MARK ITEM AS PURCHASED")
    print("\n 5] 👋🏻EXIT")

    choice=input("\n Enter ur choice here😁 ")

    if (choice=="1"):
        item=input("\n Enter the item:")
        grocery_list.append(item)
        print(f"✅ {item} appended")
    
    elif (choice=="2"):
        item=input("Enter item to remove:")
        if item  in grocery_list():
            grocery_list.remove(item)
            print(f"{item} removed")
        else:
             print(f"❌ {item} not found!")
    
    elif (choice=="3"):
        if(len(grocery_list)==0):
            print("The list is empty")
        else:
            print("The grocery list is:")
            for item in range (len(grocery_list)) :
                print(f"{item+1}. {grocery_list[item]}")
    
    elif(choice=="4"):
        if(len(grocery_list)==0):
            print("The list is empty")
        else:
            print("The grocery list is:")
            for item in range (len(grocery_list)) :
                print(f"{item+1}. {grocery_list[item]}")
            num = int(input("\nEnter number to mark as purchased: "))
            if 1 <= num <= len(grocery_list):
                print(f"✅ {grocery_list[num-1]} marked as purchased!")
                grocery_list.pop(num-1)  # Removes the purchased item
            else:
                print("❌ Invalid number!")
    
    elif (choice=="5"):
        print("Good Bye🙋🏻‍♀️")
        break

    else:
        print("INVALID CHOICE⚠️")
