#citim nr de la tastatura cu while, 0 se opreste. se stocheaza in lista
def numarprim(x):
    prim = True
    for n in range(2,x//2+1):
        if x%n==0:
            prim=False
            break
    return prim

max=0
lista_a=[]
while True:
    x=eval(input("Introduceti un numar:"))
    lista_a.append(x)
    if x==0:
        break
count=0
for p in lista_a:
    c = numarprim(p)
    if c==True:
        if p > max:
            max = p
            count = 0
        if max == p:
             count += 1
print("Numarul prim", max, "a fost afisat de", count, "ori")