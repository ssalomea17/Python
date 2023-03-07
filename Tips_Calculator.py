'''(Financial application: calculate tips) Write a program that reads the subtotal and
the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total.'''

subtotal = eval(input("Enter subtotal: "))
gratuity_rate = eval(input("Enter gratuity_rate: "))


grat = (gratuity_rate/100) * subtotal
print("Gratuity is" , str(grat) + "%")
total = subtotal + grat
print( "The total is" , str(total))
