'''
PYTHON ASSIGNMENT - 1 AMIYA VATSA (22030103)
1. Input two numbers and print there sum and difference

2. Write a program two input a side of a square and print its area

3. Input two floating numbers and print there average

4. Input two numbers and print True if one is greater than the other, otherwise False
'''

# Program 1

a = int(input("Enter a number "))
b = int(input("Enter another number "))
print("Sum is ", a + b)
print("Difference is ", a - b)

# Program 2

a = float(input("Enter the side of the square"))
ar = a * a
print("area is ", ar)

# Program 3 

a = float(input("Enter a number"))
b = float(input("Enter another number"))
avg = (a + b) / 2

print("Average is", avg)

# Program 4

a = int(input("Enter a number"))
b = int(input("Enter another number"))

if a > b:
    print("True")
else:
    print("False")