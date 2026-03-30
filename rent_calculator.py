rent = int(input("Enter flat/room rent : ₹"))
food = int(input("Enter the amount of food ordered : ₹"))
electricity = int(input("Enter the amount of electricity  : ₹"))
total_amount = (rent + food + electricity)
persons = int(input("Enter the number of persons living in the flat/room : "))
if persons==0:
    print("Invalid Number of persons must be at least one")
elif persons>1:
    print("Each person will pay : ₹", (total_amount/persons))
else:
    print("Person will pay : ₹", total_amount)

print("---------------BILL SUMMARY---------------------")
x= (rent/persons)
print("Rent: ₹",x)
y= (food/persons)
print("Food: ₹",y)
z= (electricity/persons)
print("Electricity: ₹",z)
print(f'Your total bill :',x+y+z)


