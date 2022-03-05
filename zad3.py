# Zadanie 3

a = input("Wprowadź pierwszą liczbę: ")
b = input("Wprowadź drugą liczbę: ")

a = int(a)
b = int(b)

dod = a + b
odj = a - b
mn = a * b
dz = a / b
pot = a**b
reszta = a % b

print("Wybierz opcję: \n 1. Dodawanie \n 2. Odejmowanie \n 3. Mnożenie \n 4. Dzielenie \n 5. Potęgowanie \n 6. Reszta z dzielenia")

x = input("Wpisz opcję od 1 do 6: ")
x = int(x)

if x > 6 or x < 1:
    print("Nieprawidłowa opcja")
elif x == 1:
    print(dod)
elif x == 2:
    print(odj)
elif x == 3:
    print(mn)
elif x == 4:
    print(dz)
elif x == 5:
    print(pot)
elif x == 6:
    print(reszta)