import math
number = float(input("Insert number: "))
 
w, f = math.modf(number)
 
w = round(w, 6)
 
while w != int(w):
    w *= 10
 
finNumber = int(math.pow(10, (int(math.log(f,10)) + 1)) * w + f)
 
sum = 0
while finNumber > 0:
    sum += finNumber % 10
    finNumber //= 10
 
print(int(sum))