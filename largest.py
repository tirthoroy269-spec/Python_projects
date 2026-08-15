list=[]
print("Enter 5 numbers")
list.append(int(input()))
list.append(int(input()))
list.append(int(input()))
list.append(int(input()))
list.append(int(input()))
list.sort(reverse=True)
print("The largest number is",list[0])