# nr sa fie prim
def prim(nr):
    for index in range(2, nr//2+1):
        if nr%index==0:
            return False
    return True

x=int(input("Numarul este = "))
var = prim(x)
print(var)

#do while

max=0
while True:
    x=eval(input("Introduceti un numar:"))
    p = prim(x)
    if p==True:
        if x > max:
            max = x
            count = 0
        if max == x:
            count += 1
    if x==0:
        break
print("Numarul prim", max, "a fost afisat de", count, "ori")