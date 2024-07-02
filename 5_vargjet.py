#Vargjet ne Python

print("Vargjet ne Python")

print('Vargjet ne Python')

#Slice ne Python

x = "Pershendetje!"
print(x[0])
print(x[1])

print(x[-1])

print(x[2:5])

print(x[:5])

print(x[2:])

print(x[-5:-2])

print(x[-5:])

print(x[:-2])
print(x[::2])
print(x[::3])
print(x[::-1])
print(x[2:8:2])

#Bashkimi i vargjeve
a = "Pershendetje"
b = "te gjitheve"

c = a + " " +  b
print(c)


#Funksioni format() ne Python

emri = "Albani"
mosha = 25
txt = "Une jam {}, dhe jam {} vjec."
print(txt.format(emri, mosha))

print("Une jam {0}, dhe jam {1} vjec.".format(emri, mosha))

#Funksioni F-String ne Python

emri = "Albani"
mosha = 25

txt = f"Une jam {emri}, dhe jam {mosha} vjec."
print(txt)

cmimi = 50
taksa = 0.16
totali = f"Totali i faturës është {cmimi * (1 + taksa)}"
print(totali)

print(f"Totali i faturës është {cmimi * (1 + taksa) : .2f}")


#Escape karakteret ne Python

txt = "Vendosja e nje pjese te caktuar ne \"thonjza\" te dyfishta"
print(txt)

#Metodat e vargjeve ne Python
#len()
txt = "I love apples, apple are my favorit fruit"
print(len(txt))

#upper()
print(txt.upper())

#lower()
print(txt.lower())

#replace()
print(txt.replace("apple", "banana"))

#split()
print(txt.split(","))

#strip()
txt = "        I love apples, apple are my favorit fruit       "
print(txt.strip())

#find()
txt = "I love apples, apple are my favorit fruit"
print(txt.find("apple"))

#count()
print(txt.count("apple"))