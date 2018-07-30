numbers=[2,4,6,8,10,12,14]

for i in range(len(numbers)):
    if i>=len(numbers)-1-i:
        break

    else:
        temp=numbers[i]
        numbers[i]=numbers[len(numbers)-1-i]
        numbers[len(numbers)-1-i]=temp


print("뒤집어진 리스트:"+str(numbers))