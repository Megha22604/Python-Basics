# NUMBER Guessing Program

secret_no= 22

number=int(input("Enter a number: "))
while(number!=secret_no):
    if(number<secret_no):
        print("Guess a bit bigger number😁")
    else:
        print("Guess a bit smaller number😁")
    number=int(input("Enter a number"))

if(number==secret_no):
    print("------------CONGRATULATIONS---------")