
str1 = 'mynamei  sashish'

list1 = []

for i in str1:
    list1 += i

len_string = len(list1)

for i in range(len_string):
    for j in range(i+1,len_string):
        if(list1[i] > list1[j]):
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp


print('ascending oredr in list',list1)
print('***********************************************************')
str2 = ''

for i in list1:
    str2 +=i

print('string ascending order',str2)
