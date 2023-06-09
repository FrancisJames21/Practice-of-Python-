#Write a program to find the factorial value of any number entered through the keyboard. 
"""
number = int (input("Enter a number"))

if(number < 0):
    print("the number is negative so there is no factorial of the number")

else:
    print("the factorial of number is")

    fact = 1

    for i in range(1, number +1):

        fact *= i

    print(fact)  """


#================================================================================

##Two numbers are entered through the keyboard.
# Write a program to find the value of one number raised to the power of another.
"""

number_1 = int (input("Enter a  first number "))

number_2 = int (input("Eneter a second number "))

result = number_1 ** number_2

print(result)  """

#=======================================================================

## four questions in a row


"""num = 0

count = 1

while (count <= 10):

    num += count

    count += 1
    
print ( num) """

#===========================================================

"""

sum = 9

def name():

    sum = 11

    for i in range (10):

        sum = 0
        
    print (sum)

name()

print (sum)
"""

name = [ "francis ", "james ", "renu ", "shiny", "franc ", "jame ", "rani ", "shine"]
count =1
for i in range (0,len(name)):
    
    
    print( count,"hello", name[i])
    count += 1 