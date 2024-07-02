#Operatoret ne Python

#Operatoret Aritmetik
# + Mbledhje
# - Zbritje
# * Shumezim
# / Pjestim
# % Modulus
# ** Fuqizimi
# // Pjesëtim i plotë

x = 10
y = 2
print("x + y = ", x + y) #Mbledhje
print("x - y = ", x - y) #Zbritje
print("x * y = ", x * y) #Shumezim
print("x / y = ", x / y) #Pjestim
print("x % y = ", x % y) #Modulus
print("x ** y = ", x ** y) #Fuqizimi
print("x // y = ", x // y) #Pjesëtim i plotë

#Operatoret e caktimit
# = Caktimi
# += Mbledhje dhe caktim
# -= Zbritje dhe caktim
# *= Shumezim dhe caktim
# /= Pjestim dhe caktim
# %= Modulus dhe caktim
# **= Fuqizim dhe caktim
# //= Pjesëtim i plotë dhe caktim

x = 10 #Caktimi
print(x)
x += 3 #Mbledhje dhe caktim
print(x)
x -= 3 #Zbritje dhe caktim
print(x)
x *= 3 #Shumezim dhe caktim
print(x)
x /= 3 #Pjestim dhe caktim
print(x)
x %= 3 #Modulus dhe caktim
print(x)
x **= 3 #Fuqizim dhe caktim
print(x)
x //= 3 #Pjesëtim i plotë dhe caktim
print(x)


#Operatoret i krahasimit
# == E barabarte
# != E pabarabarte
# > Me e madhe se
# < Me e vogel se
# >= Me e madhe ose e barabarte
# <= Me e vogel ose e barabarte

x = 10
y = 2
print("x == y = ", x == y) #E barabarte
print("x != y = ", x != y) #E pabarabarte
print("x > y = ", x > y) #Me e madhe se
print("x < y = ", x < y) #Me e vogel se
print("x >= y = ", x >= y) #Me e madhe ose e barabarte
print("x <= y = ", x <= y) #Me e vogel ose e barabarte


#Operatoret Logjike
# and Kushti i dyfishte
# or Kushti i shkalle
# not Kushti i kundert

x = 10
print(x > 5 and x < 15) #Kushti i dyfishte
print(x > 5 and x > 15) #Kushti i dyfishte
print(x > 5 or x < 15) #Kushti i shkalle
print(x > 5 or x > 15) #Kushti i shkalle
print(not(x > 5 and x < 15)) #Kushti i kundert


#Operatoret identiteti
# is Nese variablat jane te njejta
# is not Nese variablat nuk jane te njejta

x = ["apple", "banana"]
y = ["apple", "banana"]

z = x
print("Operatoret identiteti:")
print(x is z) #Nese variablat jane te njejta
print(x is y) #Nese variablat nuk jane te njejta
print(x is not z) #Nese variablat nuk jane te njejta
print(x == y) #Nese variablat jane te njejta


#Operatoret i anëtarësimit
# in Nese ekziston nje vlere
# not in Nese nuk ekziston nje vlere

x = ["apple", "banana"]
print("Operatoret i anëtarësimit:")
print("banana" in x) #Nese ekziston nje vlere
print("orange" in x) #Nese nuk ekziston nje vlere
print("orange" not in x) #Nese nuk ekziston nje vlere


#Operatoret e perparesise 
# ()
# **
# +x, -x, ~x
# *, /, //, %
# +, -


x = 10
y = 5
z = 2

print("Operatoret e perparesise:")
print(x ** y * z + x - y / z)
print(x ** y * (z + x) - y / z)