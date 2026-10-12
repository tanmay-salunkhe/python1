# 1 check if the number is positive, negative or zero

num = int(input("Enter your number: "))

if num > 0:
    print("the number is positive")

elif num < 0:
    print("the number is negative")

else:
    print("the number is zero")


# 2 check if the number is even or odd

num = int(input("enter your number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 3 find the greater of two numbers

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if num1 > num2:
    print(num1, "is greater")
elif num2 > num1:
    print(num2, "is greater")
else:
    print("both numbers are equal")


# 4 find the greatest of three numbers

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(num1, "is the greatest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the greatest")
else:
    print(num3, "is the greatest")


# 5 check if a person is eligible to vote

age = int(input("enter your age: "))

if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")


# 6 check whether a year is a leap year

year = int(input("enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# 7 check if a character is a vowel or consonant

letter = input("enter a character: ").lower()

if letter in "aeiou":
    print("vowel")
else:
    print("consonant")


# 8 check whether a number is divisible by 5 and 11

num = int(input("enter your number: "))

if num % 5 == 0 and num % 11 == 0:
    print("divisible by both 5 and 11")
else:
    print("not divisible by both 5 and 11")


# 9 check if a number is a multiple of both 3 and 7

num = int(input("enter your number: "))

if num % 3 == 0 and num % 7 == 0:
    print("multiple of both 3 and 7")
else:
    print("not a multiple of both 3 and 7")


# 10 assign grades based on marks

marks = int(input("enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 0:
    print("Grade F")
else:
    print("invalid marks")


# 11 check if a character is uppercase or lowercase

letter = input("enter a character: ")

if letter.isupper():
    print("uppercase")
elif letter.islower():
    print("lowercase")
else:
    print("not an alphabet")


# 12 find whether the entered alphabet is a vowel using if-elif

letter = input("enter an alphabet: ").lower()

if letter == "a":
    print("vowel")
elif letter == "e":
    print("vowel")
elif letter == "i":
    print("vowel")
elif letter == "o":
    print("vowel")
elif letter == "u":
    print("vowel")
else:
    print("not a vowel")


# 13 check if three sides can form a triangle

a = int(input("enter side 1: "))
b = int(input("enter side 2: "))
c = int(input("enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("triangle can be formed")
else:
    print("triangle cannot be formed")


# 14 determine the type of triangle

a = int(input("enter side 1: "))
b = int(input("enter side 2: "))
c = int(input("enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("not a valid triangle")


# 15 find the largest among four numbers

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
num4 = int(input("enter fourth number: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print(num1, "is the largest")
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    print(num2, "is the largest")
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print(num3, "is the largest")
else:
    print(num4, "is the largest")


# 16 check whether a number is a three-digit number

num = int(input("enter your number: "))

if 100 <= abs(num) <= 999:
    print("it is a three-digit number")
else:
    print("it is not a three-digit number")


# 17 calculate electricity bill using slab rates
# first 100 units = Rs 5, next 100 = Rs 7, next 100 = Rs 10, above 300 = Rs 12

units = int(input("enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
elif units <= 300:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
else:
    bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 12

print("electricity bill = Rs", bill)


# 18 calculate income tax based on income slabs
# up to 3L = nil, 3-7L = 5%, 7-10L = 10%, 10-12L = 15%, 12-15L = 20%, above 15L = 30%

income = int(input("enter your annual income: "))

if income <= 300000:
    tax = 0
elif income <= 700000:
    tax = (income - 300000) * 0.05
elif income <= 1000000:
    tax = 20000 + (income - 700000) * 0.10
elif income <= 1200000:
    tax = 50000 + (income - 1000000) * 0.15
elif income <= 1500000:
    tax = 80000 + (income - 1200000) * 0.20
else:
    tax = 140000 + (income - 1500000) * 0.30

print("income tax = Rs", tax)


# 19 check if a student passes (minimum 35 marks in each subject)

m1 = int(input("enter marks of subject 1: "))
m2 = int(input("enter marks of subject 2: "))
m3 = int(input("enter marks of subject 3: "))

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("student passed")
else:
    print("student failed")


# 20 find whether a number is within a given range

num = int(input("enter your number: "))
start = int(input("enter range start: "))
end = int(input("enter range end: "))

if start <= num <= end:
    print("number is within the range")
else:
    print("number is outside the range")


# 21 simple calculator using if-elif-else

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
op = input("enter operator (+, -, *, /): ")

if op == "+":
    print("result =", num1 + num2)
elif op == "-":
    print("result =", num1 - num2)
elif op == "*":
    print("result =", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("result =", num1 / num2)
    else:
        print("cannot divide by zero")
else:
    print("invalid operator")


# 22 check if a year is a century leap year

year = int(input("enter year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print(year, "is a century leap year")
    else:
        print(year, "is a century year but not a leap year")
else:
    print(year, "is not a century year")


# 23 determine the season based on the month number

month = int(input("enter month number (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month >= 3 and month <= 5:
    print("Summer")
elif month >= 6 and month <= 9:
    print("Monsoon")
elif month == 10 or month == 11:
    print("Autumn")
else:
    print("invalid month number")


# 24 find the number of days in a month

month = int(input("enter month number (1-12): "))

if month in (1, 3, 5, 7, 8, 10, 12):
    print("31 days")
elif month in (4, 6, 9, 11):
    print("30 days")
elif month == 2:
    year = int(input("enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29 days")
    else:
        print("28 days")
else:
    print("invalid month number")


# 25 check whether a password meets minimum conditions

password = input("enter your password: ")

if len(password) < 8:
    print("password must be at least 8 characters long")
elif not any(ch.isdigit() for ch in password):
    print("password must contain at least one digit")
elif not any(ch.isupper() for ch in password):
    print("password must contain at least one uppercase letter")
elif not any(ch.islower() for ch in password):
    print("password must contain at least one lowercase letter")
else:
    print("password is valid")


# 26 determine ticket price based on age category

age = int(input("enter your age: "))

if age < 0:
    print("invalid age")
elif age <= 5:
    print("ticket price: Free")
elif age <= 17:
    print("ticket price: Rs 100")
elif age <= 59:
    print("ticket price: Rs 200")
else:
    print("ticket price: Rs 120 (senior citizen)")


# 27 calculate discount based on purchase amount

amount = float(input("enter purchase amount: "))

if amount >= 10000:
    discount = amount * 0.20
elif amount >= 5000:
    discount = amount * 0.10
elif amount >= 2000:
    discount = amount * 0.05
else:
    discount = 0

print("discount =", discount)
print("final amount =", amount - discount)


# 28 check if a person is eligible for a driving license

age = int(input("enter your age: "))
eyesight = input("is your eyesight normal? (yes/no): ").lower()

if age >= 18 and eyesight == "yes":
    print("eligible for driving license")
elif age < 18:
    print("not eligible: age must be 18 or above")
else:
    print("not eligible: eyesight condition not met")


# 29 login system with username and password validation

username = input("enter username: ")
password = input("enter password: ")

if username == "admin" and password == "admin123":
    print("login successful")
elif username != "admin":
    print("invalid username")
else:
    print("incorrect password")


# 30 menu-driven program using if-elif-else

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("enter your choice: "))

    if choice == 5:
        print("exiting program")
        break

    if choice in (1, 2, 3, 4):
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))

        if choice == 1:
            print("result =", num1 + num2)
        elif choice == 2:
            print("result =", num1 - num2)
        elif choice == 3:
            print("result =", num1 * num2)
        else:
            if num2 != 0:
                print("result =", num1 / num2)
            else:
                print("cannot divide by zero")
    else:
        print("invalid choice")
