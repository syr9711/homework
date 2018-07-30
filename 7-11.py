numbers=[]

i=0
while i<10:
    numbers.append(i+1)
    i=i+1
print(numbers)

i=0
while i<len(numbers):
    if numbers[i]%2==0:
        del numbers[i]
    else:
        i=i+1

print(numbers)

numbers.insert(0,20)
print(numbers)

numbers.sort()
print(numbers)

