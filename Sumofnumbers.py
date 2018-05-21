print("Calculating the sum of two numbers10.")
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
x1 = x
y1 = y
r = 0
if (x < y):
    y = y + 1
    for i in range (x, y):
        r = r + x
        x += 1
    print ("the sum of", x1, "to", y1, "is", r)

elif (x > y):
    x += 1
    for i in range (x, y):
        r = r + y
        y += 1
    print ("the sum of", y1, "to", x1, "is", r)