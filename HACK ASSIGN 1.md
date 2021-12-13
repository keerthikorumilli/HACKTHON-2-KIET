Write a Python program to accept the user's first and last name and then getting them printed in
the the reverse order with a space between first name and last name.


```python
a=input("Enter the first name : ")
b=input("Enter the second name : ")
print("Full name of the user is " + b + " "+ a)
```

    Enter the first name : k
    Enter the second name : k
    Full name of the user is k k
    

Write a program which will find all such numbers which are divisible by 7 but are not a multiple
of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
comma-separated sequence on a single line.


```python
number=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5>0):
        number.append(str(x))
print (','.join(number))
```

    2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199
    

Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r
3


```python
pi = 3.1415926
radius = 6
Volume= 4/3*pi* radius**3
print('The volume of the sphere is: ',Volume)
```

    The volume of the sphere is:  904.7786687999999
    


```python
pi = 3.1415926
radius = int(input("Enter the radius of the sphere :"))
Volume= 4/3*pi* radius**3
print('The volume of the sphere is: ',Volume)
```

    Enter the radius of the sphere :8
    The volume of the sphere is:  2144.6605482666664
    

Write a program which accepts a sequence of comma-separated numbers from console and
generate a list.


```python
data= input("Enter the numbers separated by commas : ")
list = data.split(",")
print('List form of given numbers : ',list)
```

    Enter the numbers separated by commas : 3,2,4
    List form of given numbers :  ['3', '2', '4']
    

Write a Python program to reverse a word after accepting the input from the user.
Sample Output
Input word: Ineuron
Output: noruenl


```python
a = "Ineuron" [::-1]
print(a)
```

    noruenI
    

Write a Python Program to print the given string in the format specified in the sample output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens
Sample Output:
WE, THE PEOPLE OF INDIA,
having solemnly resolved to constitute India into a SOVEREIGN, !
SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
and to secure to all its citizens


```python
print("WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a SOVEREIGN,!\n\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\t    and to secure to all its citizens")
```

    WE, THE PEOPLE OF INDIA,
    	 having solemnly resolved to constitute India into a SOVEREIGN,!
    		 SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
    		    and to secure to all its citizens
    

Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*


```python
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
for m in range(n-1,0,-1):
    for n in range(m):
        print("*", end=" ")
    print()
```

    9
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * * * * * * 
    * * * * * * * 
    * * * * * * * * 
    * * * * * * * * * 
    * * * * * * * * 
    * * * * * * * 
    * * * * * * 
    * * * * * 
    * * * * 
    * * * 
    * * 
    * 
    


```python

```
