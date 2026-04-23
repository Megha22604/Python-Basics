print("--------CALCULATOR--------")

def add():
    n1=float(input("Enter 1st number: "))
    n2=float(input("Enter 2nd number: "))  
    result=n1+n2
    print(f"THE RESULT IS {result}")

def sub():
    n1=float(input("Enter 1st number: "))
    n2=float(input("Enter 2nd number: "))  
    diff=n1-n2
    print(f"THE RESULT IS {diff}")

def mul():
    n1=float(input("Enter 1st number: "))
    n2=float(input("Enter 2nd number: "))  
    product=n1*n2
    print(f"THE RESULT IS {product}")

def div():
    n1=float(input("Enter 1st number: "))
    n2=float(input("Enter 2nd number: "))  
    if n2==0:
        print("NOT VALID ♾️")
        
    else:
        division=n1/n2
        print(f"THE RESULT IS {division}")

def mod():
    n1=float(input("Enter 1st number: "))
    n2=float(input("Enter 2nd number: "))  
    modulo=n1%n2
    print(f"THE RESULT IS {modulo}")

while True:
    
    print("\n 1 . Add➕")
    print("\n 2 . Sub➖")
    print("\n 3 . Mul✖️")
    print("\n 4 . divide➗")
    print("\n 5 . Mod %")
    print("\n 6 . EXIT👋🏻😁")

    choice=input("\n Enter ur choice: ")
   
    if choice=="1":
        add()
    
    elif choice=="2":
        sub()
    
    elif choice=="3":
        mul()
    
    elif choice=="4":
        div()
    
    elif choice=="5":
        mod()

    elif choice=="6":
        print("BYEEEEEEE(●'◡'●)👋🏻")
        break

    else:
        print("INVALID CHOICE ❌⚠️")
    
