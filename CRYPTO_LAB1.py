#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python function to check if a given integer is a prime number or not

def prime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n < 2:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print(prime(n))


# In[2]:


#Write a Python function that counts the number of prime factors of a given integer

def prime_factors(n):
    count = 0
    factors = []  
    for i in range(2, n + 1):
        while n % i == 0:
            count += 1
            factors.append(i) 
            n //= i
    return count,factors

n = int(input("Enter a number: "))
count,factors=prime_factors(n)
print("number of prime factors:",count)
print("The prime factors are:",factors)


# In[3]:


#Implement the Euclidean Algorithm in Python to find the greatest common divisor (gcd) of two given integers

def gcd_of_numbers(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd_of_numbers(a - b, b)
    return gcd_of_numbers(a, b - a)

a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))
print(gcd_of_numbers(a, b))


# In[4]:


#Write a Python function to find the least common multiple (LCM) of two given integers

def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm

a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))
print(lcm(a, b))


# In[ ]:




