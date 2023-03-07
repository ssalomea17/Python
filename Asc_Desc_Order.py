# nr din maxim 9 cifre
# cifre in ordine cresc/descresc

n=123456789
m=987654321
count=0
counter=0
aux=n
aus=m
while n!=0:
    ultima=n%10
    n=n//10
    penultima=n%10
    if ultima>penultima:
        count=count+1
    else:
        break
print(len(str(aux)))
if count==len(str(aux)):
    print("Ordonat crescator")

while m!=0:
    ultima=m%10
    m=m//10
    penultima=m%10
    if ultima>penultima:
        counter=counter+1
    else:
        break
#print(len(str(aux)))
if counter==len(str(aus)):
    print("Ordonat descrescator")
else:
    print("Nu e ordonat descrescator")