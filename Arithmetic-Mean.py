# Cunoscandu-se limitele intregi a, b ale unui interval si un sir de n valori,
# sa se realizeze un program care determina media aritmetica a numerelor citite,
# pentru care suma cifrelor apartine intervalului [a,b]

def interval(a,b,nr):
    suma=0
    while nr!=0:
        ultima=nr%10
        nr=nr//10
        suma=suma+ultima
    if suma>=a and suma<b:
        return True
    return False

n=eval(input("De cate ori:"))
a=eval(input("a= "))
b=eval(input("b= "))
suma=0
count=0
for x in range(0,n):
    q=eval(input("Q="))
    if interval(a,b,q)==True:
        suma=suma+q
        count=count+1
ma=suma/count
print(ma)
print(suma)
print(count)

