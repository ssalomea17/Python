# 43. Se citeste de la tastatura, un sir de n numere reale. Realizati un program care determina suma maxima a doua numere din sir.
# Exemplu: Pentru n=4 si valorile 8, 3, 8 5 se va afita 16.

max1=0
max2=0
n=1
while n!=0:
    n=eval(input("introdu numere:"))
    if n>max1:
        if max1>max2:
            max2=max1
        max1=n
        continue
    if n>max2:
        max2=n
        print(max2)
suma=max1+max2
print(suma)

lista=[4,5,12,60,84]
max1=max(lista)
lista.remove(max1)
max2=max(lista)
print("Suma celor mai mari 2 numere este: " + str(max1+max2))
print(f"Suma celor mai mari 2 numere este: {max1+max2}")