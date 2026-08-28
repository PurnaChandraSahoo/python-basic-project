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

hash_dict = dict()

for i in n:
    if i in hash_dict:
        hash_dict[i] += 1
    else:
        hash_dict[i] = 1
for j in m:
    if j > 10 or j < 1:
        print(j,"-",0)
    elif j in hash_dict:
        print(j,"-",hash_dict[j])
    else:
        print(j,"-",0)

# for elif and else , place we also write -> print(j,"-",hash_dict.get(j,0))