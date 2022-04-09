#!/usr/bin/env python
# coding: utf-8

# Typecasting
# -------------------

# In[1]:



#First understand python only take str data type as input by default from user
#Until and unless you will not define the type in which you want interpretor to read


# In[1]:


Typesomething = input()
print(Typesomething)
print(type(Typesomething))


# In[3]:


#Let's understand by one more example
Typesomething = input()
print(Typesomething)
print(type(Typesomething))


# In[4]:


#Try onemore
Typesomething = input()
print(Typesomething)
print(type(Typesomething))

So let's say you have defined user to give data in any specific type, You are getting some patterns in this data that you can achieve with some operations that you can't perform on this data type but you would have achieved it if it was of that data type which accept those operation. Then type casting is very useful. Let's understand by example:-
1) You have strings of number and you are noticing a pattern that every other string of number is increasing by 5 and on basis of that you want to meet some condition and print it then you can convert it into integer type to perform count += 5 airthmetic operation.
2) You have Lists from two member of house to by grocerry for them and you want to get out common items from these two lists which means you can perform intersection here if it is set because intersection is a operation of sets. You can change your list to set perform this intersection option and then you can change the resultant set back to list. 
# In[23]:


a=(input("give your numbers "))
print(a)
print(type(a))


# In[6]:


#I have taken the very small numbers in multiple of 5 but they should have any big numbers
#Lets verify if they are increasing by 5 and if they are then I want each of them to get multiply by 2


# In[22]:


string = "5,10,15,20,25" #We know this is string we can't multiply here directly or it will just repeat it
#see false attempts below if you want 
Listx = string.split(",") #It will split the string into Listx
Listz = [int(Itemx) for Itemx in Listx] #It will convert all element of Listx to integer with list comprehension method
#print(z) Print once here just to verify Listz is getting the desired output
for ITEMZ in Listz:
    print(ITEMZ*2) 

    
   
        


# In[18]:


#FALSE ATTEMPT1
#See here its multiplying every digit by 2 not considering any two numbers operating on individual numbers
string = "10,20,30,40,50"
list(map(int,string.split(","))) #ALthough we have tried to convert it to list and then to integer
for n in string:
    if n.isdigit(): #But here we are not telling that this is two digit number before comma and its performing
        #operation on single digit
        y = int(n)
        y *= 2
        print(y)
        
        


# In[21]:


[x*2 for x in string] #Here its doing multiplication in string concatenation way and repearing each element
#even comma by 2 

Now each value got seperted in array which will be accessible by giving array index
In this example:-
y = ['5', '10', '15', '20', '25']
It is not a list it is array because it is a collection of same data type. All elements at each index value are of same data type.
y[0],y[1],y[2],y[3],y[4] all are strings that's why it is an array 
Understand it by few more example :-
a = [1,"1",2,3,4] - It is a list because a[1] is str and all others are int
a = ["brown","23","123@wxy"] - It is array because elements at all index value are string

*Now lets jump back to our problem 

# In[7]:


#Now lets say I have a array pf string numbers
# And lets try doing in this example a manual way 
y = ['5', '10', '15', '20', '25']
print(y)


# In[8]:


Outputlist = []
for items in y:
    if items[0].isdigit:
        y = int(items)
        print(y)


# In[ ]:


# These two example explain well different methods how typecasting makes data scientists job easier to
# to work on several operations 
# We took two small examples for visualization but for very large amount of data we work with several other
# methods available in python like lambda function, list comprehension method, user defined functions to use 
# along woth typecasting for being more specific 


# In[ ]:




