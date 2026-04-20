for i in range(100) :
    if(i%3==0 and i%5==0):
         print("-----FIZZBUZZ-----")
    elif(i%3==0):
        print("_____FIZZ_____")
    elif(i%5==0):
        print("|||||BUZZ|||||")
    else:
        print(i)
       