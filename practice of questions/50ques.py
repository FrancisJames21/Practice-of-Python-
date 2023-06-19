"""Certainly! Here are 50 coding questions in Python:

1. Write a program to print "Hello, World!".#
2. Write a program to swap two variables.#
3. Write a program to check if a number is even or odd.#
4. Write a program to find the factorial of a number.#
5. Write a program to check if a number is prime.#
6. Write a program to generate Fibonacci series.#
7. Write a program to check if a string is a palindrome.
8. Write a program to find the largest element in an array.
9. Write a program to reverse a string.#
10. Write a program to sort an array in ascending order.
11. Write a program to count the number of vowels in a string.
12. Write a program to find the sum of digits of a number.
13. Write a program to check if a string is an anagram.
14. Write a program to find the length of a string.
15. Write a program to check if a number is a power of two.
16. Write a program to find the common elements between two arrays.
17. Write a program to calculate the area of a circle.
18. Write a program to check if a year is a leap year.
19. Write a program to reverse a number.
20. Write a program to convert a decimal number to binary.
21. Write a program to find the second largest element in an array.
22. Write a program to remove duplicates from an array.
23. Write a program to find the GCD (Greatest Common Divisor) of two numbers.
24. Write a program to convert a string to lowercase.
25. Write a program to check if a string is a valid email address.
26. Write a program to calculate the sum of all even numbers in a range.
27. Write a program to find the maximum of three numbers.
28. Write a program to find the square root of a number.
29. Write a program to check if a string is a palindrome using recursion.
30. Write a program to find the median of an array.
31. Write a program to reverse the words in a string.
32. Write a program to check if a number is Armstrong number.
33. Write a program to convert a binary number to decimal.
34. Write a program to count the occurrences of a character in a string.
35. Write a program to find the smallest element in an array.
36. Write a program to check if a string is a valid URL.
37. Write a program to calculate the average of numbers in an array.
38. Write a program to find the LCM (Least Common Multiple) of two numbers.
39. Write a program to check if a string is a palindrome without using extra space.
40. Write a program to reverse a sentence.
41. Write a program to check if a string is a valid parentheses expression.
42. Write a program to remove a specific element from an array.
43. Write a program to convert a decimal number to octal.
44. Write a program to count the number of words in a string.
45. Write a program to find the sum of natural numbers using recursion.
46. Write a program to find the number of occurrences of a substring in a string.
47. Write a program to find the ASCII value of a character.
48. Write a program to find the largest prime factor of a number.
49. Write a program to check if a string is a valid palindrome ignoring spaces.
50. Write a program to reverse a linked list.

These coding questions cover a variety of concepts in Python programming and should help you practice and enhance your coding skills."""


# print("hello world")

# Program to swap two variables

"""print("before swapping")

a = 4 
b = 3

print("a =",a,",", "b =",b)

print("After Swapping")
 
demo = a

a = b

b = demo

print("a =",a,",", "b =",b)"""

#=============================================


"""num = int (input("Enter a number "))

if(num % 2 == 0 ):
    print("the number in even")

else :
    print("the number is odd")"""

#=================================================================


"""number = int (input("enter a number"))

for i in range(1,number ):

    number *= i # here 
    
    
print(number)
"""

#===========================================================

"""number = int (input("Enter a number here "))

# for i in range(0,number +1):

if (number == 2  ):
    print("prime number ")

elif(number % 2 ==0):
    print("it not a prime number ")

else :
    print(number,"is a prime number  ")"""

#===============================================================






"""num1 = int (input("Enter a number here "))

num2 = int (input("Enter a number here "))

print(num1)

limit = 100

while(num2 <= limit):

    print(num2)

    num1,num2 = num2,num1 + num2
"""
#=====================================
"""
Name = ["francis ", "James" ,"Shiny", "Jmaes"]

print(Name[::-1])"""

#==================================================

# how to find a gratest number in array


A = [232423,24,2434,34,322,323,343,]

for i in range(0,len(A)):

    print(A[i])