# (Compute GCD) Write a function that returns the greatest common divisor (GCD) of integers in a list. Use the following function header:
# def gcd(numbers):
# Write a test program that prompts the user to enter five numbers, invokes the function to find the GCD of these numbers, and displays the GCD.

def min(lista):
    min=lista[0]
    for i in lista:
        if i<min:
            min=i
    return min

# x - nr din lista
# i - nr
def gcd(lista,min):
    for i in range(min,0,-1):
        count=0
        for x in lista:
            if x%i!=0:
                count=count+1
        if count==0:
            return i

lista=[4,6,12]
a=min(lista)
b=gcd(lista,a)
print(b)