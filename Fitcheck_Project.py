def bmi(a,b):
    c=b/(a*a)
    return(c)
def bmr_for_male(w,h,a):
    bmr=(10*w)+(6.25*h)-(5*a)+5
    return(bmr)
def bmr_for_female(w,h,a):
    bmr=(10*w)+(6.25*h)-(5*a)-161
    return(bmr)
print("=========================================\n   NutriFit: An Algorithmic Health & Nutrition Analytics Engine\n   Analytics Engine - Main Menu")
while True:
    print("=========================================\n1. BMI(Body Mass Calculator)\n2. BMR(Basal Metabolic Rate)\n3. TDEE(Total Daily Energy Expenditure)\n4. Bodyfat\n0. Exit\n=========================================")
    choice=int(input("Enter a choice:"))
    if choice==1:
        height=float(input("Enter height in metre:"))
        weight=float(input("Enter weight:"))
        d=bmi(height,weight)
        if d<=18.5:
            print("BMI is",d,"kg/m² and the person is underweight")
        elif d<=24.9:
            print("BMI is",d,"kg/m² and the person is healthy weight")
        elif d<=29.9:
            print("BMI is",d,"kg/m² and the person is overweight")
        else:
            print("BMI is",d,"kg/m² and the person is Obese")
    elif choice==2:
        g=input("Person is male or female:")
        hieght=float(input("Enter hieght:"))
        weight=float(input("Enter wieght:"))
        age=int(input("Enter age "))
        if g=="male":
            c=bmr_for_male(weight,hieght,age)
            print("basal metabolic rate is:",c,"kilocalories per day")
        if g=="female":
            c=bmr_for_female(weight,hieght,age)
            print("basal metabolic rate is:",c,"kilocalories per day")
    elif choice==3:
        gender=input("Person is male or female")
        hieght=float(input("Enter hieght:"))
        weight=float(input("Enter wieght:"))
        age=int(input("Enter age "))
        if gender=="male":
            c=bmr_for_male(weight,hieght,age)
            print("basal metabolic rate is",c,"kilocalories per day")
        elif gender=="female":
            c=bmr_for_female(weight,hieght,age)
            print("basal metabolic rate is",c,"kilocalories per day")
        activity_level=input("Activity level is Sedentary or Lightly Active or Moderately Active or Very Active or Extra Active:")
        if activity_level=="Sedentary":
            tdee=c*1.2
            print("Total Daily Energy Expenditure of Body is","kilocalories per day")
        elif activity_level=="Lightly Active":
            tdee=c*1.375
            print("Total Daily Energy Expenditure of Body is",tdee,"kilocalories per day")
        elif activity_level=="Moderately Active":
            tdee=c*1.55
            print("Total Daily Energy Expenditure of Body is",tdee,"kilocalories per day")
        elif activity_level=="Very Active":
            tdee=c*1.725
            print("Total Daily Energy Expenditure of Body is",tdee,"kilocalories per day")
        elif activity_level=="Extra Active":
            tdee=c*1.9
            print("Total Daily Energy Expenditure of Body is",tdee,"kilocalories per day")
        else:
            print("Enter a valid input")
    elif choice==4:
        gender=input("Person is Adult male or Adult female or Boy or Girl:")
        height=float(input("Enter height: "))
        weight=float(input("Enter weight: "))
        age=float(input("Enter age: "))
        d=bmi(height,weight)
        if gender=="Adult male":
            BFP=1.2*d+0.23*age-16.2
            print("Body fat is",BFP,"%")
        if gender=="Adult female":
            BFP=1.2*d+0.23*age-5.2
            print("Body fat is",BFP,"%")
        if gender=="Boy":
            BFP=1.51*d+0.70*age-2.2
            print("Body fat is",BFP,"%")
        if gender=="Girl":
            BFP=1.51*d+0.70*age-1.4
            print("Body fat is",BFP,"%")
    elif choice==0:
        print("Thank you")
        break
    else:
        print("Enter a valid choice")
