x = input("Enter an integer for x: ")
y = input("Enter an integer for y: ")
z = input("Enter a decimal for z: ")

productxy = int(x) * int(y)
productxyz = int(x) * int(y) * float(z)
xmod2 = int(x) % 2
ymod2 = int(y) % 2
zmod2 = float(z) % 2

print("Product of x and y is " + str(productxy) + "\nProduct of x, y, and z is " + str(productxyz) + "\n" + str(x) + " mod 2 is " + str(xmod2) + "\n" + str(y) + " mod 2 is " + str(ymod2) + "\n" + str(z) + " mod 2 is " + str(zmod2))