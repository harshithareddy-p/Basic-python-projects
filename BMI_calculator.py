print("BMI (Body Mass Index) Calculator")

user_weight = int(input("Enter your weight in Kg's:"))
user_height = int(input("Enter your height in Cm's:"))

BMI = (user_weight/((user_height/100)**2))
print("Your BMI Value = ", BMI)

if(BMI<18.5):
     print("You are Underweight")

elif(18.5<BMI<24.9):
     print("You have Normal weight")

elif(25<BMI<29.9): 
     print("You are Overweight")

else:
     print("You have Obesity")
