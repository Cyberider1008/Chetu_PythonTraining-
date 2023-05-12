list1 = [7,8,2,1,3,6,4,5,15]

len_list = len(list1)

for i in range(len_list):
    for j in range(i+1, len_list):
        if(list1[i] > list1[j]):
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] =temp

print('ascending order',list1)
