# GRADE CALCULATOR

marks=int(input("ENTER UR MARKS: "))

if(90<marks<100):
    print(" YOUR GRADE IS: A+")
    print("Excellent! 🏆")
elif(80<=marks<=89):
    print(" YOUR GRADE IS: A")
    print("Very Good! 🎉")
elif(70<=marks<=79):
    print(" YOUR GRADE IS: B")
    print("Good job! 👍")
elif(60<=marks<=69):
    print(" YOUR GRADE IS: C")
    print("Can improve 📚")
elif(50<=marks<=59):
    print(" YOUR GRADE IS: D")
    print("Need more effort 💪")
else:
    print(" YOUR GRADE IS: F")
    print("Fail. Try again! ❌")
