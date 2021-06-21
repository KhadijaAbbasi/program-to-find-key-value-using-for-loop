list=[]
for i in range (0,20):
    list.append(input('enter number: '))
print(list)
key=input('Enter key value you want to search: ')
count=0
for x in range(len(list)):
    if int(key)==int(list[x]):
        count=count+1
print(count)