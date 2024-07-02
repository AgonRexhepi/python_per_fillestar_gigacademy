#Variablat ne Python

#Variablat ne Python nuk kane nevoje per te deklaruar tipin e tyre para se te perdoren.
x = 5
y = "Pershendetje"

print(x)
print(y)

#Castimi i tipit te variablave
x = str(3)    # x tani eshte '3'
y = int(3)    # y tani eshte 3
z = float(3)  # z tani eshte 3.0

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#Emertimi i variablave

emri = "Beni"
print(emri)

_emri = "Beni"
print(_emri)

emri_1 = "Beni"
print(emri_1)

#Variablat nuk mund te fillojne me numer
#2_emri = "Beni"
#print(2_emri)

#Variablat nuk mund te kene simbole speciale
#emri-1 = "Beni"
#print(emri-1)

EMRI = "Beni"
print(EMRI)


#Caktimi i shume variablave
x, y, z = "Portokalli", "Banane", "Molle"
print(x)
print(y)
print(z)

ngjyrat = ["e gjelber", "e kuqe", "e verdhe"]
x, y, z = ngjyrat
print(x)
print(y)
print(z)

#Variablat globale

x = "i mire"

def myfunc():
    print("Python eshte " + x)

myfunc()

#Variablat lokale

x = "i mire"

def myfunc():
    x = "fantastik"
    print("Python eshte " + x)

myfunc()

print("Python eshte " + x)

#Ndryshimi i variablave globale brenda funksioneve

x = "i mire"

def myfunc():
    global x
    x = "fantastik"
    print("Python eshte " + x)

myfunc()

print("Python eshte " + x)