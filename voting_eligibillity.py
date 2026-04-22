#age based voting eligibility

age=int(input("Enter ur AGE: "))
citizen_of=input("Are u INDIAN?(Yes/No): ")

if(age>=18 and citizen_of=="Yes"):
    print("✅ You are eligible to vote")
elif (age>= 18 and citizen_of == "No") :
    print("❌ Not eligible to vote")
elif (age < 18 and citizen_of == "Yes"):
    print("❌ Not eligible to vote")
elif (age < 18 and citizen_of == "No"):
    print("❌ Not eligible to vote")


