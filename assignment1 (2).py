# 1 find the data type of every value in a mixed list

mixed_list = [10, "Hello", 3.14, True, [1, 2], {'a': 1}, (5, 6)]

for item in mixed_list:
    print("Value:", item, "-> Type:", type(item).__name__)


# 2 convert a nested list into a tuple of tuples

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

tuple_of_tuples = tuple(tuple(sub) for sub in nested_list)

print("Original list:", nested_list)
print("Tuple of tuples:", tuple_of_tuples)


# 3 remove all duplicate values from a mixed list while preserving the original order

mixed_list = [1, "apple", 2, "apple", 3.14, 1, True, "banana"]

seen = set()
unique_list = []

for item in mixed_list:
    marker = (type(item), item)
    if marker not in seen:
        seen.add(marker)
        unique_list.append(item)

print("Preserved unique list:", unique_list)


# 4 check whether a number is a power of 2 using operators

num = int(input("Enter your number: "))

if num > 0 and (num & (num - 1)) == 0:
    print("The number is a power of 2")

else:
    print("The number is not a power of 2")


# 5 swap two numbers using bitwise XOR

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("Before swap:", num1, num2)

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print("After swap:", num1, num2)


# 6 find whether a number is divisible by both 4 and 6 using logical operators

num = int(input("enter your number: "))

if num % 4 == 0 and num % 6 == 0:
    print("The number is divisible by both 4 and 6")

else:
    print("The number is not divisible by both 4 and 6")


# 7 calculate the total electricity bill using different unit rates

units = float(input("enter electricity units consumed: "))

if units <= 100:
    bill = units * 3.50

elif units <= 200:
    bill = (100 * 3.50) + (units - 100) * 5.00

elif units <= 300:
    bill = (100 * 3.50) + (100 * 5.00) + (units - 200) * 7.50

else:
    bill = (100 * 3.50) + (100 * 5.00) + (100 * 7.50) + (units - 300) * 10.00

print("Total electricity bill: Rs.", bill)


# 8 check whether three sides can form a triangle

a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("The three sides form a valid triangle")

else:
    print("The three sides cannot form a triangle")


# 9 determine the type of triangle

a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral triangle")

    elif a == b or b == c or a == c:
        print("Isosceles triangle")

    else:
        print("Scalene triangle")

else:
    print("Not a valid triangle")


# 10 create a simple ATM menu

balance = 10000.0

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Current balance: Rs.", balance)

elif choice == 2:
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print("Updated balance: Rs.", balance)
    else:
        print("Invalid deposit amount")

elif choice == 3:
    amount = float(input("Enter withdrawal amount: "))
    if 0 < amount <= balance:
        balance -= amount
        print("Please collect cash. Updated balance: Rs.", balance)
    elif amount > balance:
        print("Insufficient balance")
    else:
        print("Invalid amount")

elif choice == 4:
    print("Thank you for using our ATM service")

else:
    print("Invalid choice")


# 11 calculate income tax based on different tax slabs

income = float(input("enter your annual taxable income: "))

if income <= 250000:
    tax = 0.0

elif income <= 500000:
    tax = (income - 250000) * 0.05

elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20

else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

print("Calculated income tax: Rs.", tax)


# 12 create a menu-driven calculator using if-elif

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    print("Result:", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")

else:
    print("Invalid choice")


# 13 print all prime numbers between 1 and n

n = int(input("enter value of n: "))

print("Prime numbers between 1 and", n, ":")

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print()


# 14 find the factorial of a number using a loop

num = int(input("enter your number: "))

if num < 0:
    print("Factorial does not exist for negative numbers")

else:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of", num, "is", fact)


# 15 print the Fibonacci series up to n terms

terms = int(input("enter number of terms: "))

a = 0
b = 1
count = 0

print("Fibonacci series:")

while count < terms:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1

print()


# 16 check whether a number is an Armstrong number

num = int(input("enter your number: "))

digits = str(num)
power = len(digits)
total_sum = sum(int(d) ** power for d in digits)

if total_sum == num:
    print("The number is an Armstrong number")

else:
    print("The number is not an Armstrong number")


# 17 reverse a number and check if it is a palindrome

num = int(input("enter your number: "))

temp = abs(num)
rev = 0

while temp > 0:
    rev = (rev * 10) + (temp % 10)
    temp = temp // 10

if num < 0:
    rev = -rev

print("Reversed number:", rev)

if num == rev:
    print("The number is a palindrome")

else:
    print("The number is not a palindrome")


# 18 find the Greatest Common Divisor (GCD) of two numbers

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

a = num1
b = num2

while b != 0:
    temp = b
    b = a % b
    a = temp

print("The GCD of", num1, "and", num2, "is", a)


# 19 write a function to check if a string is a palindrome

def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

string_input = input("enter a string: ")

if is_palindrome(string_input):
    print("The string is a palindrome")

else:
    print("The string is not a palindrome")


# 20 write a function to count vowels and consonants in a string

def count_vowels_consonants(text):
    vowels = set("aeiouAEIOU")
    v_count = 0
    c_count = 0
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

text_input = input("enter a string: ")
v, c = count_vowels_consonants(text_input)

print("Vowels:", v)
print("Consonants:", c)


# 21 create a function to calculate simple and compound interest

def calculate_interest(p, r, t, n=1):
    si = (p * r * t) / 100
    ci = p * ((1 + (r / (100 * n))) ** (n * t)) - p
    return si, ci

p = float(input("enter principal amount: "))
r = float(input("enter annual rate of interest: "))
t = float(input("enter time in years: "))

si, ci = calculate_interest(p, r, t)

print("Simple Interest: Rs.", round(si, 2))
print("Compound Interest: Rs.", round(ci, 2))


# 22 write a function to return all factors of a number

def find_factors(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i * i != n:
                factors.append(n // i)
    return sorted(factors)

num = int(input("enter a positive number: "))
print("Factors of", num, "are:", find_factors(num))


# 23 write a function to find the second-largest number in a list

def get_second_largest(numbers):
    unique = list(set(numbers))
    if len(unique) < 2:
        return None
    unique.sort(reverse=True)
    return unique[1]

nums = [12, 45, 2, 45, 89, 34, 89]

print("Numbers list:", nums)
print("Second largest number:", get_second_largest(nums))


# 24 merge two lists without duplicates

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

merged = list(dict.fromkeys(list1 + list2))

print("List 1:", list1)
print("List 2:", list2)
print("Merged list without duplicates:", merged)


# 25 find the second-largest and second-smallest elements

nums = [15, 3, 9, 21, 3, 45, 9, 21]

unique_sorted = sorted(list(set(nums)))

if len(unique_sorted) >= 2:
    print("Second smallest element:", unique_sorted[1])
    print("Second largest element:", unique_sorted[-2])

else:
    print("List must have at least two distinct elements")


# 26 rotate a list to the left by k positions

def rotate_left(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return lst[k:] + lst[:k]

arr = [10, 20, 30, 40, 50, 60]
k = int(input("enter rotation shift k: "))

print("Original list:", arr)
print("Rotated list:", rotate_left(arr, k))


# 27 separate even and odd numbers into two lists

numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]

even_list = [x for x in numbers if x % 2 == 0]
odd_list = [x for x in numbers if x % 2 != 0]

print("Original list:", numbers)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)


# 28 find the common elements between two lists

list_a = [1, 3, 5, 7, 9, 11]
list_b = [2, 3, 5, 7, 12, 14]

common = list(set(list_a) & set(list_b))

print("List A:", list_a)
print("List B:", list_b)
print("Common elements:", sorted(common))


# 29 count the frequency of each element in a tuple

tup = ('a', 'b', 'a', 'c', 'b', 'a', 'd', 'e', 'd')

frequency = {}

for item in tup:
    frequency[item] = frequency.get(item, 0) + 1

print("Tuple:", tup)

for key, count in frequency.items():
    print(key, "appears", count, "times")


# 30 find the union, intersection, and difference of two sets

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Difference (B - A):", set_b - set_a)


# 31 check whether one set is a subset of another

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)

if set1.issubset(set2):
    print("Set 1 is a subset of Set 2")

else:
    print("Set 1 is not a subset of Set 2")


# 32 count the frequency of words in a sentence

sentence = input("enter a sentence: ")

words = sentence.lower().split()
word_counts = {}

for word in words:
    cleaned = word.strip(".,!?:;'\"")
    word_counts[cleaned] = word_counts.get(cleaned, 0) + 1

print("Word frequency count:")

for word, count in word_counts.items():
    print(word, ":", count)


# 33 create a dictionary from two lists (keys and values)

keys = ["name", "roll_no", "branch", "semester"]
values = ["Tanmay", 101, "Computer Engineering", 6]

student_dict = dict(zip(keys, values))

print("Keys:", keys)
print("Values:", values)
print("Created dictionary:", student_dict)


# 34 sort a dictionary by its values

student_scores = {'Alice': 88, 'Bob': 95, 'Charlie': 78, 'David': 92}

sorted_dict = dict(sorted(student_scores.items(), key=lambda item: item[1]))

print("Original dictionary:", student_scores)
print("Sorted by values:", sorted_dict)


# 35 read a text file and count the number of lines, words, and characters

filename = "sample.txt"

with open(filename, "w") as f:
    f.write("Python programming is powerful.\nEasy to learn and versatile.\nFile handling practice.")

line_count = 0
word_count = 0
char_count = 0

with open(filename, "r") as file:
    for line in file:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)

print("File:", filename)
print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)


# 36 copy only the even-numbered lines from one file to another

source_file = "source.txt"
target_file = "even_lines.txt"

with open(source_file, "w") as f:
    for i in range(1, 7):
        f.write("Line " + str(i) + "\n")

with open(source_file, "r") as src, open(target_file, "w") as tgt:
    for line_num, line in enumerate(src, start=1):
        if line_num % 2 == 0:
            tgt.write(line)

print("Even numbered lines copied successfully")


# 37 handle invalid integer input using try-except

while True:
    try:
        age = int(input("enter your age: "))
        print("Valid age received:", age)
        break

    except ValueError:
        print("Invalid input! Please enter an integer only.")


# 38 handle file-not-found errors while reading a file

filename = input("enter file path to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    print("Error: The file does not exist")


# 39 create a random password generator using the random and string modules

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

length = int(input("enter password length: "))
print("Generated password:", generate_password(length))


# 40 use the datetime module to calculate the number of days between two dates

from datetime import datetime

date_str1 = input("enter first date (YYYY-MM-DD): ")
date_str2 = input("enter second date (YYYY-MM-DD): ")

d1 = datetime.strptime(date_str1, "%Y-%m-%d")
d2 = datetime.strptime(date_str2, "%Y-%m-%d")

difference = abs((d2 - d1).days)
print("Number of days between dates:", difference)