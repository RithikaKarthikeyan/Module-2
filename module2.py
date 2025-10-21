#EX-01

a=16
b=bin(a)
print(b)

#EX-02

def result(a,b):
    print(a%b)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
result(a,b)

#EX-03

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
f = lambda a , b : a + b
print("The sum is : ",f(a,b))

#EX-04

from math import factorial

n = int(input("Enter the number of rows: "))

for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=' ')
    print()

#EX-05

n = int(input("Enter a number: "))
temp = n
rev = 0

while temp > 0:
    rev = (10 * rev) + temp % 10
    temp = temp // 10

if rev == n:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")
