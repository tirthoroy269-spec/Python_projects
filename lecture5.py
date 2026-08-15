# # # for i in range(1, 6):
# # #     for j in range(i):
# # #         print(i, end=" ")
# # #     print()

# # # list=[1,4,9,16,25,36,49,64,81,100]
# x=36
# f=2
# for i in range(len(list)):
#     if(x==list[i]):
#         print("Found at index ",i)
#         f=1
#         break
#     else:
#         continue
# if(f==2):
#     print("Not found")

# b = int(input("Enter the last number: "))
# i = 1
# total = 0

# while i <= b:
#     total = total + i
#     i = i + 1

# print(total)

# n=int(input("Enter the last digit "))
# for i in range(1,n+1):
#     f=1;
#     for j in range(i,1,-1):
#         f=f*j
#     print(f)

# n=int(input("Enter the last number"))
# sum=0
# for i in range(n+1):
#    sum=sum+i
# print(sum)

# n=int(input("Enter the last digiit "))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)

# char=input("Enter a word ")
# l=len(char)
# count=0
# for i in range (l):
#     if("aeiouAEIOU".find(char[i])!=-1):
#         count=count+1
# print("No. of vowels ",count)

# char=input("Enter a string ")
# l=len(char)
# newstr=""
# for i in range(l-1,-1,-1):
#     newstr=newstr+char[i]
# print("Reverse of the string ",newstr)

# list=[35,32,10,62,78,44,51,12]
# largest=list[0]
# idx=0
# for i in range(len(list)):
#     if(list[i]>largest):
#         largest=list[i]
#         idx=i
#     else:
#         continue
# print("Largest",largest,"\nIndex",idx)

# n=int(input("Enter the range "))
# a=0 ; b=1 ; c=1 
# print(a)
# print(b)
# for i in range(n-2):
#   print(c)
#   a=b
#   b=c
#   c=a+b

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(1, 6):
#     # Print spaces
#     for j in range(5 - i):
#         print(" ", end="")

#     # Print stars
#     for k in range(2 * i - 1):
#         print("*", end="")

#     # Move to the next line
#     print()

# k=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(k, end="")
#         k=k+1
#     print()

# list=[35,32,10,62,78,44,51,12]
# for i in range(len(list)):
#     t=0
#     for j in range(len(list)-1):
#         if(list[j]>list[j+1]):
#             t=list[j]
#             list[j]=list[j+1]
#             list[j+1]=t
# print(list[len(list)-2]) 

# str=input("Enter a string ").upper().replace(" ","")
# l=len(str)
# checkstr=""
# for i in range(l):
#     char=str[i]
#     count=0
#     for j in range(l):
#         if(checkstr.find(char)==-1):
#             if(char==str[j]):
#                 count=count+1
#             else:
#                 continue 
#     if(checkstr.find(char)==-1):
#      print(char,":",count) 
#     checkstr=checkstr+char        

# n = int(input("Enter the number of rows: "))

# def fact(a):
#     p = 1
#     for i in range(1, a + 1):
#         p *= i
#     return p

# for i in range(n):

#     # Print leading spaces
#     for j in range(n - i):
#         print(" ", end="")

#     # Print Pascal's Triangle values
#     for j in range(i + 1):
#         value = fact(i) // (fact(j) * fact(i - j))
#         print(value, end=" ")

#     # Move to the next row
#     print()
