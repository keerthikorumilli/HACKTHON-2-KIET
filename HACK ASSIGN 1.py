#!/usr/bin/env python
# coding: utf-8

# 
# Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

# In[1]:


a=input("Enter the first name : ")
b=input("Enter the second name : ")
print("Full name of the user is " + b + " "+ a)


# Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.

# In[15]:


number=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5>0):
        number.append(str(x))
print (','.join(number))


# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r
# 3

# In[4]:


pi = 3.1415926
radius = 6
Volume= 4/3*pi* radius**3
print('The volume of the sphere is: ',Volume)


# In[5]:


pi = 3.1415926
radius = int(input("Enter the radius of the sphere :"))
Volume= 4/3*pi* radius**3
print('The volume of the sphere is: ',Volume)


# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.

# In[12]:


data= input("Enter the numbers separated by commas : ")
list = data.split(",")
print('List form of given numbers : ',list)


# Write a Python program to reverse a word after accepting the input from the user.
# Sample Output
# Input word: Ineuron
# Output: noruenl

# In[16]:


a = "Ineuron" [::-1]
print(a)


# Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens
# Sample Output:
# WE, THE PEOPLE OF INDIA,
# having solemnly resolved to constitute India into a SOVEREIGN, !
# SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
# and to secure to all its citizens

# In[18]:


print("WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a SOVEREIGN,!\n\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\t    and to secure to all its citizens")


# Create the below pattern using nested for loop in Python.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# In[17]:


n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
for m in range(n-1,0,-1):
    for n in range(m):
        print("*", end=" ")
    print()


# In[ ]:




