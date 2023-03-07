# Se citeste de la tastatura, un sir de n numere naturale.
# Realizati un program care determina numarul total de cifre al tuturor numerelor prime din sir.

def prim(nr):
    for index in range(2, nr//2+1):
        if nr%index==0:
            return False
    return True

def count(nr):
    count=0
    while nr!=0:
        nr=nr//10
        count=count+1
    return count

suma=0
n=1
while n!=0:
    n=eval(input("introdu numere:"))
    if prim(n)==True:
        a=count(n)
        suma=suma+a
print(suma)