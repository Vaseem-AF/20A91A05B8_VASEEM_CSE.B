#Factors of a number

n=int(input('Enter the number whose factors is to be found '))
i=1
print('The factors of numbers are : ')
while i in range (i,n+1):
       if (n%i==0):
        print(i)
        i=i+1

       else :
        i=i+1
        
#output :

Enter the number whose factors is to be found 6
The factors of number are : 
1
2
3
6
