'''distanta dintre 2 puncte citite de la tastatura import math math.sqrt'''

import math
x1 = eval(input("X1: "))
y1 = eval(input("Y1: "))
x2 = eval(input("X2: "))
y2 = eval(input("Y2: "))
dist = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
print("Distance is ",dist)