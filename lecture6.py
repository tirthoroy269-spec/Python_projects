# cities=["delhi","gurgao","kolkata","mumbai","pune","chennai"]

# def length(list):
#     print(len(list))

# length(cities)

# def fact(n):
#     if(n==0 or n==1):
#        return 1
#     else:
#         return n*fact(n-1)
# b=fact(5)
# print(b) 

# def sum(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return n+sum(n-1)

# print(sum(10))

# list=[1,2,3,4,5,6,7,8,9]
# l=len(list)
# def show(a,idx):
#    if(idx==len(list)):
#       return
#    print(a[idx],end=" ")
#    show(a,idx+1)

# show(list,0)

# def fibo(n):
#     if(n==1):
#         return 0
#     if(n==2):
#         return 1
#     return fibo(n-1)+fibo(n-2)

# print(fibo(6))

# def exp(x,n):
#     if(n==0):
#         return 1
#     return x*exp(x,n-1)

# print(exp(2,4))

# def sum(n):
#     if(n==0):
#        return 0
#     if(n%2==0):
#         return n+sum(n-2)
#     else:
#      return  sum(n-1)

# print(sum(15))

# def convert(num):
#     if(num==0):
#         return
#     convert(num//2)
#     print(num%2,end=" ")

# convert(43)

# def rev(str,idx):
#     if(idx==-1):
#         return
#     print(str[idx])
#     rev(str,idx-1)

# print(rev("BALLS",len("BALLS")-1))

# a='E'
# def count(str,idx):
#     if(idx==len(str)):
#        return 0
#     if(str[idx]==a):
#       return 1+count(str,idx+1)
#     else:
#        return count(str,idx+1)

# c=count("ELITE",0)
# print(c)
