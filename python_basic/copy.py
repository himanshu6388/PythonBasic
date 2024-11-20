# greeting = "hello world"
# print(greeting)

# age = 25 
# age_as_string = str(age)
# print("I am " + age_as_string + " years old")

# name  = input("What is your name?")
# age = input("What is your age?")
# num = input("Enter your Favorite Number:")

# num = num * 2
# print(" Your Favorite Number Twice is: " + num)

# #Conver age to an integer (optional , depending on your use case)
# age = int(age)
# print("Hello, " + name + "! you are " + str(age) + " years old")


# age = int(input("Enter your age:"))

# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age <= 60:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

# For  Loop

for  number in range (1,6):
    print(number)

for char in "python":
    print(char)

# While Loop
count = 1

while count <= 8:
    print(count)
    count += 1

# Break Statement

for i in range(10):
    if i == 5:
        break
    print(i)

# Continue Statement
print("Continue Statement")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# else statement

print("else statement")
for i in range(5):
    print(i)
else:
    print("Loop is completed")

# Odd or Even Checker
print("Odd Even Chcker Program")
number = int(input("Enter a number:"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Fizz Buzz Problem

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Factorial Calculation

print("Factorial Calculation Progam.")

n = int(input("Enter a number for calculate  factorial:"))

factorial = 1
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0 or n == 1:
    print("Factorial of", n, "is 1")
else:
    for i in range(1, n+1):
        factorial *= i
        print("Factorial of",n , "is", factorial)

# Using Recursion 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a Number :"))
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))