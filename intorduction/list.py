A= ["fscsdc","djdsinvir","cdijfeifjie","emjofijeo9o"]

print(A)

count= 1

for i in range(0,len(A)):

    print(count,"hello", A [i])

    count += 1


# name = [ "francis ", "james ", "renu ", "shiny", "franc ", "jame ", "rani ", "shine"]
# count =0
# for i in range (0,len(name)):
#       count += 1 
#       print( count,"hello", name[i])
  

# name = [ "francis ", "james ", "renu ", "shiny", "franc ", "jame ", "rani ", "shine"]

# print(name[::-1]) # to revese the array

#=============================================================================================

## More functions of list 
"""
name = [ "francis ", "james ", "renu ", "shiny", "franc ", "jame ", "rani ", "shine"]

name.append("snum") # A.append() add a value in  the end of the list by default

print(name)

name.insert(0,"dog") # it help to insert a value a any number of index

print(name)

name.pop(0)# it helps to remove any index value and empty pop remove last value of index by default

print(name) """

# tuples are similer to list but you can nit chnage its value untill you typecast the tuple into a list
"""

A = ("name", "work", "suman", "sajal")

B = A[::-1]

print(B) """

## it helps to meger to list by + opertor
"""

A = [1,2,4,5]

B = [3,5,7,98 ]

C= (A+B)

print(C)  """

# you can create a list in a list and you can access their value by give a index number again
"""
A = [1,2,3,4,5,6,"francis",[100,425]]

print(A[7][0])"""

