#Exercise 1:
'''
def factorial(nbr):
    total=1 #The minimum factorial for all nbr=>0 is 1 since 0!=1
    while(nbr!=0):
        total*=nbr #the factorial is just the product from 1 to nbr
        nbr-=1
    return total

nbr=int(input())
while(nbr<0):
    nbr=int(input("Enter a positive number"))

print(factorial(nbr))
'''
#Exercise 2:
'''
def divisors(nbr):
    l1=[]
    for i in range(1,nbr+1): #nbr+1 so we include nbr
        if(nbr%i==0):
            l1.append(i) #add the divider to the list 
    return l1
    

nbr=abs(int(input("Please enter an integer")))
print(divisors(nbr))
'''

#Exercise 3:
'''
def reverse(phrase):
    phrase2=""
    for i in range(len(phrase)-1, -1, -1): #len(phrase)-1 because first value is inclusive and the indexes go from 0 to n-1
        phrase2 += phrase[i]
    return phrase2

phrase=input("please input a string")
print(reverse(phrase))
'''

#Exercise 4:
'''
def even(l1):
    l2=[]
    for i in l1:
        if (i%2==0):
            l2.append(i)
    return l2

n=int(input("Enter integers. Enter -1 to stop"))
l1=[]
while (n!=-1):
    l1.append(n)
    n=int(input("Enter integers. Enter -1 to stop"))
print(even(l1))
'''

#Exercise 5:
'''
def check(string):
    total=False #The default state will be false for all of the required checkboxes 
    upper=False
    lower=False
    special=False
    digit=False
    if (len(string)>8):
        total=True
    for i in string: #only one char is needed to pass each requirement so we check is char individually
        if(i.isupper()):
            upper=True
        if(i.islower()):
            lower=True
        if(i.isdigit()):
            digit=True
        if i in ["#","$","?","!"]:
            special=True
    if (total and upper and lower and special and digit): #all checkboxes need to be true for it to be a strong password
        print("Strong password")
    else:
        print("Weak password")

string=input("Please enter a password")
check(string)
'''
#Exercise 6:

def ip(ipv4):
    l1=ipv4.split(".")  #splits the string up to each . and puts the parts in a list

    if len(l1) != 4:  #to check how many dots there s
        print("Invalid number of octets")
        return
    
    for i in l1:
        if not i.isdigit():#very important to do check this first since if there s an empty string we will run into an error trying to reach the index on the next one
            print(i + " is not a number")
            return

        if len(i) > 1 and i[0] == "0":
            print("Leading 0 in octet")
            return
        
        number = int(i)

        if number < 0 or number > 255:
            print("Octet out of range 0-255")
            return
    print("Valid IP")
ipv4 = input("Enter an IP: ")
ip(ipv4)