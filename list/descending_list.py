
list1 = [67,76,34,14,98,64,34,67]

len_list = len(list1)

for i in range(len_list):
    for j in range(i+1, len_list):
        if(list1[i]<list1[j]):
            temp =list1[j]
            list1[j] =list1[i]
            list1[i] = temp

print('descending order',list1)
