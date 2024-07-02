#Unazat ne Python

#For Loop ne Python
#While Loop ne Python
#Nested Loops ne Python


#For Loop ne Python
#1
numrat = [1, 2, 3, 4, 5]
for x in numrat:
    print(x)

#2
mystr = "Pershendetje"

for var in mystr:
    print(var)

#3
ngjyrat = ["e bardhe", "e kuqe", "e verdhe"]

for x in ngjyrat:
    print(x)

#Range() ne For Loop
#4
for x in range(6):
    print(x)

#5
for x in range(2, 6):
    print(x)

#6
for x in range(2, 30, 3):
    print(x)


#While Loop ne Python
print("While Loop ne Python")

i = 1
while i < 6:
    print(i)
    i += 1

#Nested Loops ne Python
print("Nested Loops ne Python")

#1
numrat = [1, 2, 3]
shkronjat = ["a", "b", "c"]

for x in numrat:
    for y in shkronjat:
        print(x, y)


#Break Statement ne Python
print("Break Statement ne Python")

#1
print("for loop")
for x in range(6):
    if x == 3:
        break
    print(x)

#2
print("while loop")
i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1

#Continue Statement ne Python
print("Continue Statement ne Python")

#1
print("for loop")
for x in range(6):
    if x == 3:
        continue
    print(x)

#2
print("while loop")
i = 1
while i < 6:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

#Pass Statement ne Python
print("Pass Statement ne Python")

#1
print("for loop")
for x in [0, 1, 2]:
    pass

def funksioni():
    pass

class Klasa:
    pass
