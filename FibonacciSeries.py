n = int(input("How Many terms of Fibonacci series you want"))

x = 0
y = 1
z = 0

if (n <= 0):
    print("Enter Positive Number")
elif (n == 1):
    print("The Fibonacci series is ", x)
else:
    print("The Fibonacci series is ")
    while (z <= n):
        print(z)
        x = y
        y = z
