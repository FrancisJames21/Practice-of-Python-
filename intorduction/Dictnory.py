"""
name = {

"breakfast" : 9 ,
"lunch" : 2,
"Dinner" : 7
}

print(name["lunch"])"""


"""name  ["num"]= 9 # if key is not present in dict so it will create it
name ["lunch"]= 3 # this is how you can chnage the present value the key

name.pop("num") # it will help to delete a key with its value

print(name.keys())# it can print all keys 

print(name.values())# it will print all values

print(len(name))# it shows us the length of dict.."""

"""for key in name:

    print("keys are",key,"=","values are",name[key])# we can use it in for loop also"""


# in - key is also use in dict 
#=========================================== to get the maximum number 

"""A = [ 1,2,3,4,45,5,56,667,7]

max=A[0]

for i in range (1,len(A)):

    if(A[i]>max):

        max = A[i]

print(max)

"""
#=============================================
"""
A= {
    "francis" : 21,
    "shiny" : 20,
    "james" : 32,
    "kajal" : 45,
    "renu" : 50

    
    }

print(A["francis"])

A ["name"] = [11,2,2,]

print(A)

A["francis"]="jamesss"

print(A)

A.pop("renu")

print(A)

print(A.keys())

print(A.values())"""

#============================================= to get the frequency of the number  

A = [1,1,1,2,2,2,2,3,3,4,4,4,5,5,]

B = {}

for i in A:

    if (i  in B):

        B[i] += 1
    
    else:
        B[i] = 1

print(B)

#===============================================

    


