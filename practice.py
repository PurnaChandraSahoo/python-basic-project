#TODO: count digit:
# from math import sqrt

# n = 5845
# num = n
# count = 0
# while num > 0:
#     count = count + 1
#     num = num//10
#
# print(count)
# from math import *
# def countDigit(num):
#     return int(log10(num)+1)
#
# print(countDigit(4567))

# TODO: Check palindrome:

# num = int(input("Enter a number: "))
# n = num
# rev = 0
# while n>0:
#     newNum = n % 10
#     rev  = rev * 10 + newNum
#     n = n//10
#
# if num == rev :
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

# TODO:Find Armstrong:

# num = int(input("Enter a number: "))
# n = num
# count = 0
# while n > 0:
#     count+=1
#     n = n//10
#
# arm = 0
# n = num
# while n > 0:
#     newNum = n % 10
#     arm = ( newNum ** count ) + arm
#     n = n//10
# if arm == num:
#     print(num,"number is Armstrong")
# else:
#     print(num,"number is not Armstrong")

# TODO : Find factor or Divider :

# num = int(input("Enter a number: "))
# result = []
# for i in range(1,num+1):
#     if num % i == 0:
#         result.append(i)
# print(result)

# Another approach:

# num = int(input("Enter a number: "))
# result = []
# for i in range(1,num+1//10):
#     if num % i == 0:
#         result.append(i)
# result.append(num)
# print(result)

# Optimal solution

# num = int(input("Enter a number: "))
# result = []
# for i in range(1,int(sqrt(num))+1):
#     if num % i == 0:
#         result.append(i)
#         if num//i != i:
#             result.append(num//i)
# result.sort()
# print(result)

# TODO : Dictionary :

# list1 = [1,5,7,8,41,1,45,41,5,2,45,5,1,41,2,3,78,36,415,5,5,5,8,966,7,5,7,8]
# frequency = {} # or we can write dict()
# for i in range (0,len(list1)):
#     if list1[i] in frequency:
#         frequency[list1[i]] += 1
#     else:
#         frequency[list1[i]] = 1
# print(frequency)

# Another approach :

# list1 = [1,5,7,8,41,1,45,41,5,2,45,5,1,41,2,3,78,36,415,5,5,5,8,966,7,5,7,8]
# frequency = dict()
# for i in range (0,len(list1)):
#     frequency[list1[i]] = frequency.get(list1[i],0) +1
# print(frequency)

# TODO : HASHING

n = [5,3,2,2,1,5,5,7,5,10,1,10]
m = [10,111,1,9,5,67,2]

# Approach ->1

# for i in m :
#     count = 0
#     for j in n:
#         if j == i:
#             count += 1
#     print(i,"--",count)

# Approach -> 2

# hash_list = [0] * 11
#
# for i in n:
#     hash_list[i] += 1
#
#
# for j in m:
#     if j < 1 or j>10:
#         print(j,"-",0)
#     else:
#         print(j,"-",hash_list[j])

# Approach -> 3

# hash_dict = dict()
#
# for i in n:
#     if i in hash_dict:
#         hash_dict[i] += 1
#     else:
#         hash_dict[i] = 1
# for j in m:
#     if j > 10 or j < 1:
#         print(j,"-",0)
#     elif j in hash_dict:
#         print(j,"-",hash_dict[j])
#     else:
#         print(j,"-",0)

# for elif and else , place we also write -> print(j,"-",hash_dict.get(j,0))

# string hashing ->
# Uppercase ASCII Values (A–Z)A: 65 B: 66 C: 67 D: 68 E: 69 F: 70  G: 71 H: 72 I: 73 J: 74 K: 75 L: 76 M: 77 N: 78 O: 79
# P: 80 Q: 81 R: 82 S: 83 T: 84 U: 85 V: 86 W: 87 X: 88 Y: 89 Z: 90

# Lowercase ASCII Values (a–z)a: 97 b: 98 c: 99 d: 100 e: 101 f: 102 g: 103 h: 104 i: 105 j: 106 k: 107 l: 108 m: 109
# n: 110 o: 111 p: 112 q: 113 r: 114 s: 115 t: 116 u: 117 v: 118 w: 119 x: 120 y: 121 z: 122

# s = "azyxyyzaaaanwdej"
#
# q = ["d","a","y","z","w","n"]
#
# hash_list = [0] * 26
#
# for i in s :
#     ascii_value = ord(i)
#     index = ascii_value - 97
#     hash_list[index] += 1
# for  j in q :
#     ascii_value = ord(j)
#     index = ascii_value - 97
#     print(hash_list[index])


# TODO : Recursion ->

# count = 0
# def printname(count):
#     if count == 5:
#         return
#     print("hello world")
#
#     printname(count + 1)
# printname(0)

# Print 10 to 1 using recursion ->
# It is called tail

# def fun(i,n):
#     if i>n :
#         return
#     fun(i+1,n)
#     print(i)
# fun(1,10)

# print 1 to 10 using recursion ->
# It is called head
# def fun(i,n):
#     if i==n:
#         return
#     print(i)
#     fun(i+1,n)
# fun(1,11)

# print 1 to 10 using tail ->

# def fun(i):
#     if i == 0 :
#         return
#     fun(i-1)
#     print(i)
# fun(10)

# Functional recursion ->

# def fun(i):
#     if i == 1:
#         return 1
#     return fun(i-1)+i
# print(fun(5))

# Find factorial of n using recursion ->

# def factorial(n):
#     if n ==1 :
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

# reverse an array ->

# li = [5 , 7 , 3 , 2 , 6 , 1 ,5 , 9]
#
# def fun(li,l,r):
#     if l >= r:
#         return
#     li[l], li[r] = li[r], li[l]
#     fun(li,l+1,r-1)
# fun(li,0,len(li)-1)
# print(li)

# check a no. is palindrome or not , using recursion ->

# num = int(input("enter a number:"))
#
# def fun(num,rev=0):
#
#     if num <= 0:
#         return rev
#     r = num % 10
#
#     return fun(num//10,rev * 10 + r)
# rev = fun(num)
# if num == rev :
#     print("true")
# else:
#     print("false")

# find out string palindrome ->

# name = input("Enter your name : ")
# revName = name[:1:-1]
# revName = "".join(reversed(name))

# Using Recursion ->
# def palindrome(name,l,r):
#     if l >= r:
#         return True
#     if name[l] != name[r]:
#         return False
#
#     return palindrome(name,l+1,r-1)
# if palindrome(name,0,len(name)-1):
#     print("True")
# else:
#     print("False")


