#Reverse of the number

number=int(input('Enter the number '))
summation=0
while (number!=0):
    remainder=number%10
    summation=summation*10+remainder
    number=number//10

print('The reverse number is %d' %summation)    

#output :
Enter the number 67347
The reverse number is 74376
