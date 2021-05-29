#Checking whether entered number is prime or not

n=int(input('Enter the number '))
i=1
count=0
print('The factors of ', n, 'are : ' )

while (i<=n):
    if (n%i==0):
        print(i, end=" ")
        count=count+1
    i=i+1
print('\nsince the number has %d factors it is ' %count)

if (count==2):
    print('a prime number')
else :
    print('not a prime number')
