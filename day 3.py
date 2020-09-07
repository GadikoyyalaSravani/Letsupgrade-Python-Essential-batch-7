# 1 Question
# landing of a Plane
s =input("Enter the altitude of the Plane in fts:")
s=int('s')
for (s<=1000):
    print("Safe for landing\n")
    print("Please land the Plane")
elif (1000<s<5000):
    print("Come down to 1000ft for landing\n")
else (s>5000):
    print("Go around and try later ")


# 2 Question
# Prime numbers between 1-200 using for loop
x = 1
y = 200
print("Prime numbers between", x , "and", y , "are:")
for num in range(x,y + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
