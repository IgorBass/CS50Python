exspression = input("Expression: ")

x, y, z = exspression.split(" ")

z = float(z)
x = float(x)

if y=='+':
    print(x+z)
elif y=='-':
    print(x-z)
elif y=='*':
    print(x*z)
elif y=='/':
    print(x/z)
    