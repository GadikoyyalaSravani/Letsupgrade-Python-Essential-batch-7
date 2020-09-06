#1 list and its default functions

#Adding element to a list. 
List = ['sravani', 'venkata', 1996, 2000] 
List.append(20) 
print(List)

#inserting element in particular index 
List = ['sravani', 'venkata',1997, 2000] 
List.insert(2,'pragati college')      
print(List)

#adding element from one list to other
List1 = [1, 2, 3] 
List2 = [2, 3, 4, 5] 
# Add List2 to List1 
List1.extend(List2)         
print(List1) 
# Add List1 to List2 now 
List2.extend(List1)  
print(List2) 

#addition of elements in list
List = [1, 2, 3, 4, 5] 
print(sum(List)) 

#count of elements in list (repetitions count)
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.count(1)) 

#Lenth of list
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(len(List)) 

#2 Dictionary & its default funtions

#Creating Python Dictionary
dict = {}
#Accessing Elements from Dictionary
dict = {'name': 'Jack', 'age': 26}
print(dict['name'])
#Changing and Adding Dictionary Elements
dict = {'name': 'Jack', 'age':26}
dict['age'] = 27
print(dict)
dict['address'] = 'Downtown'
print(dict)
#Removing elements from Dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)
print(squares.popitem())
print(squares)
squares.clear()
print(squares)
del squares
print(squares)


#3 Sets & its default functions

#Creating Python Sets
st = {1, 2, 3}
print(st)
st = {1.0, "Hello", (1, 2, 3)}
print(set)
#Modifying a set
st = {1, 3}
print(st)
st.add(2)
print(st)
st.update([2, 3, 4])
print(st)
st.update([4, 5], {1, 6, 8})
print(st)
#Removing elements
st = {1, 3, 4, 5, 6}
print(st)
st.discard(4)
print(st)
st.remove(6)
print(st)
st.discard(2)
print(st)
st.remove(2)

#4 Tuple & explore default methods

#Creating
tup = ()
print(tup)
mtup = (1, 2, 3)
print(tup)
tup = (1, "Hello", 3.4)
print(tup)
tup = ("mouse", [8, 4, 6], (1, 2, 3))
print(tup)
#Access Tuple Elements
tup = ('p','e','r','m','i','t')
print(tup[0])    
print(tup[5])
ntup = ("mouse", [8, 4, 6], (1, 2, 3))
print(ntup[0][3])       
print(ntup[1][1])

#5 string & explore default methods 
#create a string
string = 'Hello'
print(string)
string = "Hello"
print(string)
string = '''Hello'''
print(string)
string = """Hello, welcome to the world of Python"""
print(string)
#access characters in a string
str = 'programiz'
print('str = ', str)
print('str[0] = ', str[0])
print('str[-1] = ', str[-1])
print('str[1:5] = ', str[1:5])
print('str[5:-2] = ', str[5:-2])
#change or delete a string
string = 'programiz'
string[5] = 'a'
del string[1]
#methods
"PrOgRaMiZ".lower()
'programiz'
"PrOgRaMiZ".upper()
'PROGRAMIZ'
"This will split all words into a list".split()
['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
'This will join all words into a string'
'Happy New Year'.find('ew')
7
'Happy New Year'.replace('Happy','Brilliant')
'Brilliant New Year'



