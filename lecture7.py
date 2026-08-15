# with open("Details.txt","r") as c:
#     str=c.read()
# newstr=str.replace("Java","Python")
# with open("Details.txt","w") as b:
#     b.write(newstr)

# with open("Details.txt","r") as f:
#     data=f.read()
# if "learning" in data:
#     print("Learning is present")
# else:
#     print("Learning is not present") 

# def check_for_line():
#     wrd="learning"
#     data=True
#     i=0
#     with open("Details.txt","r") as f:
#      while data:
#         data=f.readline()
#         i=i+1
#         if(wrd in data):
#            print("Word found on the line",i)
#            return
#     print("Word not found")
#     return -1
# check_for_line()

# def num():
#     n=""
#     for i in range(1,101):
#         n=n+str(i)+" "
#         if(i%10==0):
#             n=n+"\n"

#     with open("even_.txt","w") as f:
#         f.write(n)

# num()

# def print_even():
#     with open("even_.txt", "r") as f:
#         data=True
#         while data:
#             data=f.readline()
#             a=data.split()
#             l=len(a)
#             i=0
#             while (i<l):
#                 if (int(a[i])%2==0):
#                  print(a[i],end=" ")
#                 i+=1
#             print()
# print_even()
    
# def palin(str):
#     if str==str[::-1]:
#         return True
#     else:
#         return False

# def print_palin():
#     data=True
#     with open("Details.txt","r") as f:
#          while data:
#                 data=f.readline()
#                 i=0
#                 a=data.split()
#                 l=len(a)
#                 while(i<l):
#                      if(palin(a[i])):
#                           print(a[i],end=" ")
#                      i=i+1
# print_palin()

# def print_sum():
#     with open("even_.txt","r")as f:
#              num=list(map(int,f.read().split()))
#              print("Max",max(num))
#              print("Min",min(num))
#              print("Sum",sum(num))
#              print("Avg",sum(num)/len(num))
# print_sum()

# def duplicate():
#     seen = []
#     with open("dup.txt", "r") as f:
#         words = f.read().split()
#     with open("DUPLICATE.txt", "w") as g:
#         for word in words:
#             if word not in seen:
#                 g.write(word+"\n")
#                 seen.append(word)
# duplicate()

# def count():
#     up=0 ; lo=0 ; sp=0 ; spe=0 ; d=0
#     with open("Details.txt","r") as f:
#         data=f.read()
#     for words in data:
#         if(words.isupper()):
#             up=up+1
#         elif(words.islower()):
#             lo=lo+1
#         elif(words==" "):
#             sp=sp+1
#         elif(words.isdigit()):
#             d=d+1
#         else:
#             spe=spe+1
#     print("Upper case",up,"\nLower Case",lo,"\nSpaces",sp,"\nDigits",d,"\nSpecial Character",sp)
# count()

# def student_credentials():
#     with open("student.txt","r") as f:
#         tup=f.read().split()
#     l=len(tup)
#     m=tup[1]
#     name=""
#     for i in range(1,l,2):
#         if(tup[i]>m):
#             m=tup[i]
#             name=tup[i-1]
#     print("Topper",name)
#     print("Marks",m)
# student_credentials()

# def sentence():
#     with open("Details.txt","r") as f:
#         data=True
#         str=""
#         i=0
#         while data:
#           data=f.readline()
#           if(len(str)<len(data)):
#              str=data
#              i=i+1
#         print("The longest sentence:",str,"\nLine no.",i)      
# sentence()      

# with open("bruh2.txt", "x") as f:
#     pass