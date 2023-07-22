n=int(input())
while (len(str(n)) >1):
    sum=0
    for i in str(n):
        sum+=int(i)
    n=sum
if n==1:
    print('1')
else:
    print('0')
