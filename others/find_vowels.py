# find a vowels

name = "ChetuNoida".casefold()
count = 0
for i in name:
    if i in ('a','e','i','o','u'):
        count +=1
print(count)

