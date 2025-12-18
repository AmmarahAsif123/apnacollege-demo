n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# The Euclidean Algorithm
while(n2 != 0):
    t = n2
    n2 = n1 % n2
    n1 = t

hcf = n1
print("HCF of the two numbers is: ", hcf)