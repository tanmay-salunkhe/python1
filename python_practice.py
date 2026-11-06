# 1 check whether a number is even or odd

num = int(input("Enter your number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 2 find the largest of three numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(num1, "is the largest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the largest")
else:
    print(num3, "is the largest")


# 3 check whether a given number is prime

num = int(input("Enter your number: "))

if num > 1:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is prime")
    else:
        print("The number is not prime")
else:
    print("The number is not prime")


# 4 print the Fibonacci series up to n terms

terms = int(input("Enter number of terms: "))

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


# 5 find the factorial of a number using a loop

num = int(input("Enter your number: "))

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of", num, "is", fact)


# 6 reverse a string without using [::-1]

text = input("Enter a string: ")

reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text

print("Reversed string:", reversed_text)


# 7 check whether a string is a palindrome

text = input("Enter a string: ")

cleaned = "".join(c.lower() for c in text if c.isalnum())

if cleaned == cleaned[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


# 8 count the number of vowels and consonants in a string

text = input("Enter a string: ")

vowels = set("aeiouAEIOU")
v_count = 0
c_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)


# 9 find the sum of all elements in a list

numbers = [10, 20, 30, 40, 50]

total_sum = 0
for num in numbers:
    total_sum += num

print("List:", numbers)
print("Sum of all elements:", total_sum)


# 10 find the largest and smallest element in a list without using max() or min()

numbers = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

largest = numbers[0]
smallest = numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("List:", numbers)
print("Largest element:", largest)
print("Smallest element:", smallest)


# 11 remove duplicate elements from a list

original_list = [1, 2, 3, 2, 4, 1, 5, 6, 4]

unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original list:", original_list)
print("List without duplicates:", unique_list)


# 12 count how many times each element appears in a list using a dictionary

items = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

print("List:", items)
print("Element frequencies:")
for key, value in counts.items():
    print(key, ":", value)


# 13 find the second-largest number in a list

numbers = [12, 45, 2, 45, 89, 34, 89]

unique_numbers = list(set(numbers))

if len(unique_numbers) >= 2:
    unique_numbers.sort(reverse=True)
    print("List:", numbers)
    print("Second-largest number:", unique_numbers[1])
else:
    print("List must contain at least two distinct numbers")


# 14 sort a list without using sort() or sorted()

numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

# Bubble sort
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)


# 15 function that accepts a list and returns only the even numbers

def get_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = get_even_numbers(sample_list)

print("Original list:", sample_list)
print("Even numbers list:", result)


# 16 find the frequency of each character in a string

text = input("Enter a string: ")

char_freq = {}
for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1

print("Character frequencies:")
for ch, freq in char_freq.items():
    print(repr(ch), ":", freq)


# 17 check whether two strings are anagrams of each other

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

clean1 = sorted(str1.replace(" ", "").lower())
clean2 = sorted(str2.replace(" ", "").lower())

if clean1 == clean2:
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")


# 18 find all duplicate values in a list

numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]

seen = set()
duplicates = set()

for item in numbers:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("List:", numbers)
print("Duplicate values:", list(duplicates))


# 19 take a sentence and find the longest word

sentence = input("Enter a sentence: ")

words = sentence.split()
longest_word = ""

for word in words:
    cleaned_word = word.strip(".,!?:;'\"")
    if len(cleaned_word) > len(longest_word):
        longest_word = cleaned_word

print("Sentence:", sentence)
print("Longest word:", longest_word)


# 20 create a simple student marks program

print("=== Student Marks Program ===")

marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i} (out of 100): "))
    marks.append(m)

total = sum(marks)
percentage = (total / 500) * 100

print("\nTotal Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")

# Grade and result calculation
is_passed = all(m >= 35 for m in marks)

if not is_passed:
    print("Result: Failed")
    print("Grade: F")
else:
    print("Result: Passed")
    if percentage >= 75:
        print("Grade: Distinction")
    elif percentage >= 60:
        print("Grade: First Class")
    elif percentage >= 50:
        print("Grade: Second Class")
    else:
        print("Grade: Pass Class")

