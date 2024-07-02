#If...Else Statement ne Python

#if Kushti:

a = 33
b = 200
#1
if b > a:
  print("IF: b është më e madhe se a")

#2
if a > b:
  print("IF: a është më e madhe se b")

#Else Kushti:
#3
if a < b:
  print("IF: b është më e madhe se a")
else:
    print("Else: a është më e madhe se b")

#4
if a > b:
  print("IF: a është më e madhe se b")
else:
    print("Else: b është më e madhe se a")


# elif Kushti:
x = 20 
y = 30

#5
if x > y:
  print("IF: x është më e madhe se y")
elif x < y:
    print("Elif: x është më e vogël se y")
else:
    print("Else: x është e barabartë me y")

#6
var1 = 100
var2 = 100

if var1 > var2:
    print("IF: var1 është më e madhe se var2")
elif var1 < var2:
    print("Elif1: var1 është më e vogël se var2")
elif var1 == var2:
    print("Elif2: var1 është e barabartë me var2")
else:
   print("Else: vlerat nuk jane te krahasueshme")