def tuppleAdd(tup1,tup2):
    list1=[]
    for i in range(len(tup1)):
        numb=(tup1[i]+tup2[i])
        list1.append(numb)
    tup3=tuple(list1)
    print(tup3)

# tup1=(1,2,3)
# tup2=(1,2,3)
# tuppleAdd(tup1,tup2) 

def dicWrite(mydic,jsonfile):
    myfile = '{'
    items = []
    for key, value in mydic.items():
        key_str = f'"{key}"'
        
        if isinstance(value, str):
            value_str = f'"{value}"'  # Strings need double quotes
        elif isinstance(value, bool):
            value_str = 'true' if value else 'false'  # Boolean  lowercase
        elif value is None:
            value_str = 'null'  
        elif isinstance(value, (int, float)):
            value_str = str(value)  
    
        
        items.append(f'{key_str}: {value_str}')
    
    myfile+= ', '.join(items)
    myfile += '}'
    file = open(f"{jsonfile}.txt", 'w') 
    file.write(myfile)
    file.close()
   
   
def dicRead(jsonfile):
    file=open(f"{jsonfile}.txt","r")   
    content = file.read().strip()


    dict_list = []


    current_object = {}
    in_string = False
    key = ""
    value = ""
    is_key = True
    for char in content:
        if char == '"':  
            in_string = not in_string
        elif char == '{' and not in_string:  
            current_object = {}
        elif char == '}' and not in_string: 
            current_object[key.strip()] = value.strip()
            dict_list.append(current_object)
            key = ""
            value = ""
            is_key = True
        elif char == ':' and not in_string:  
            is_key = False
        elif char == ',' and not in_string: 
            current_object[key.strip()] = value.strip()
            key = ""
            value = ""
            is_key = True
        else:
            if in_string or (not in_string and char.strip() != ''):
                if is_key:
                    key += char  
                else:
                    value += char  

    return dict_list

nbr=0

while(nbr!=4):
    print("1. Sum Tuples \n2. Export JSON \n3. Import JSON \n4. Exit")
    nbr=int(input())
    if (nbr==1):
        n1=input("enter 2 tuples of the same size, leave space between each number").split()
        n2=input().split()
        tuple1=tuple(map(int,n1))
        tuple2=tuple(map(int,n2))
        tuppleAdd(tuple1,tuple2)
    elif (nbr==2):
        dic = input("Enter key-value pairs (format: key1:value1, key2:value2): ")
        json=input("Enter the name of the json file")

        input_dic = dict(item.split(":") for item in dic.split(", ")) #splits each item seperated by :(key and value) after splitting them by , (each index)

        dicWrite(input_dic,dic)
    elif(nbr==3):
        json=input("Enter the name of the json file")
        dicRead(json)
    

#Exercise 2:
'''
a.O(N^3)
b.O(N^3)
c.O(N!)
d.O(NlogN)
e.O(N)
f.O(N^2)
g.O(N^2)
h.O(N!)'''
    
        