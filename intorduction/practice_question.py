"""
## solving some questions

print("enter a number ")

num = int(input())

if(num % 4 == 0  ):

    print("number is divisible by 4")

else:
    print("number is not divisible by 4") 

 ## fizz buzz interview question    

num = int (input("enter a number "))

if (num % 3 == 0 and num % 5 == 0):
    print("FIZZ BUZZ")

else:
    if (num % 3 == 0 ):
        print("fizz")

    if (num % 5 == 0 ):
        print("fuzz")       

    """

    # using elif here 
name = "francis" 

if(name == "james " ):
    print("your name is")

elif(name == "francis"):
    print("your name is francis")
