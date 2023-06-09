
# number = 5

# sum = 0

# for i in range (1, number + 1):

#     sum += i ** 3
    
#     print (sum)

# =======================================================
"""  
print("francis is the good boy who fears the God ")

def true():
    print("and he obey the word of God")


true()
true()   """

# def adding(a , b ):
#     return a + b 

# number = adding(2 , 5)
# print(number)

# def name(go , do ):
#     return go / do 


# numbers = name(18 , 2)

# print(numbers)



# def adding(a , b):
#     return a + b 


# x = int (input("Enter a  number 1   "))

# y = int (input("Enter a number 2   "))

# ans = adding(x , y )

# print ("the sum of x and y is  ", ans)

#===============================================================

# def Is_even(a):
#     if (a % 2 == 0):
#         return True
        
#     else:
#         return False

# x = int (input("Enter a number"))

# ans = Is_even(x)

# print(ans)

#==================

# print("Enter a number for row ", end = " ")
# n = int (input())
# for i in range (1, n+1):
#     for stars in range (i):
#         print("#", end = " ")

#     print ()
     
  # to print starts as row

  #=====================================================


# Write a program to print numbers from 1 to 10.

# for i in range (1,11):
#   print(i)

#====================================================================



# Write a program to calculate the sum of first 10 natural number.

 # Initialize variables
# sum_of_numbers = 0
# counter = 1

 # Calculate the sum using a while loop
# while counter <= 10:
#     sum_of_numbers += counter
#     counter += 1

 # Print the result
# print("The sum of the first 10 natural numbers is:", sum_of_numbers)

# sum = 0 

# count = 1 

# while (count <= 10):

#   sum += count 

#   count += 1
  
# print ("the sum of natural number from 1 -10 is",sum )

#=================================================================================

  #Write a program that prompts the user to input a positive integer. It should then print the 
 # multiplication table of that number. 

# num = int (input("Enter a number "))

# if (num <= 0):
#   print ("its not a valid number Please enter a valid number ")

# else:
#   print("table of the number ", num)

#   for i in range (1,11):
#     print(num , "x", i , "=", num *i)

#===================================================================

## this is called scoping the outer verible called as a globle scoping and 
#the in inner variable called local scope

"""sum = 6

def name ():

  sum =  7

  print(sum )


name()

print (sum)
 """

 # example of list 
"""
ABC = ["a",2.4343,"c",83943]

print (ABC)  # it will print the whole list
print (len(ABC)) # it will print the length of list (by count th index number )
print(ABC[3]) # its print the index number 

print(type(ABC))  # to prints its type of data

 """

 ## slices similer to range 
"""
#A=["name", 2 , 2.2, 33, "francis ", 5,67]

#print(A[0:7:1])

for i in range (0,7,1):

  print (i)
"""

#=====================================


# cnt = 1
# A = ["a", "b ", "c"]
# for i in  A:
#   print( cnt, ".", "hello", i)
#   cnt += 1

  
 ##======================================
# A = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(A)):
#   print(i +1, ".", "hello", A [i] )


num = int (input("enter a positive number"))
if (num <0):
  print("number is negative")

else :
  print("the factorial of a number  ", num)
  
  for i in range (0,num+1):
    print(num)