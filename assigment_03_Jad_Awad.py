def calculateDigits(num):

  if (num <1):  # base case (num==0 would work too)
    return 0
  num=num//10 #floor division, we go down one digit at a time
  return calculateDigits(num)+1 #each incriment each iteration

def findMax(l1,index):
    if(index==len(l1)-1): #base case
        return l1[index] #the program will go to the last index and compare it with all the previous indexes
    max=findMax(l1,index+1) 
    if(l1[index]<max):
        return max
    else:
        return l1[index]

import re

def count_tags(html, tag):
    # Define the pattern for matching the opening and closing tag
    tag_pattern = fr'<{tag}[^>]*>(.*?)</{tag}>'
    
    # Search for the first match
    match = re.search(tag_pattern, html, re.DOTALL)
    
    if not match:
        return 0
    
    # If a match is found remove it from the  code and count it, then recursively process the remaining HTML
    remaining_html = re.sub(tag_pattern, '', html, count=1, flags=re.DOTALL)
    
    # Count 1 for the found tag, then recursively call to count remaining occurrences
    return 1 + count_tags(remaining_html, tag)


html = """
<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>"""

nbr=0

while(nbr!=4):
    print("1. Count Digits \n2. Find Max \n3. Count Tags \n4. Exit")
    nbr=int(input())
    if(nbr==1):
        digits=int(input("Please input a number"))
        print("The number of digits is "+str(calculateDigits(digits)))
    elif(nbr==2):
      l1=[]
      max=0
      while(max!=-1):
         max=int(input("Please input numbers to the list"))
         l1.append(max)
      print("The max number in the list is "+str(findMax(l1,0)))
    elif(nbr==3):
       pattern=input("Please enter a tag")
       print("The occurences of this tag is "+str(count_tags(html,pattern)))
