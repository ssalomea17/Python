count=0
factor=2
def numar_prim(nr):
    prim=True
    for n in range(2, nr//2+1):
        if nr%n==0:
            prim=False
            break
    return prim

def factor_prim(numar):
    global count
    global factor
    factor=2
    for x in range(2,numar+1):
        prim=numar_prim(x)
        if prim==True:
            if numar%x==0:
                if factor==x:
                    count=count+1
                else:
                    print("factor= "+str(factor)+" count= "+str(count))
                    factor=x
                    count=1
                numar=numar//x
                return numar,x
if __name__=="__main__":
 n=int(input("Numarul este = "))

 while True:
    n,factor=factor_prim(n)
    print(n,factor)
    if n==1:
        print("factor= " + str(factor) + " count= " + str(count))
        break

# de facut cu lista cu duplicate
# declaram lista cu 22,33,44,55. Sa numaram cate sunt