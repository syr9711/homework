n=int(input("정수를 입력하시오:"))
i=1
count=0

while i<=n:
    if n%i==0:
        print(i)
        i=i+1
        count=count+1
    else:
        i=i+1

print(n,"의 약수는 총 %d개 입니다"%(count))



