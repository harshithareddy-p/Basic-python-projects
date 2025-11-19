import random

while True:
 print("Roll the dice ?:(y/n)")
 x = input("").upper()
 if x == 'Y' :
     die1 = random.randint(1,6)
     die2 = random.randint(1,6)
     print('(',die1,',',die2,')')
 elif x == 'N':
     print("okay game terminated")
     break
 else:
     print("invalid")
