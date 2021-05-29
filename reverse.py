#Reverse of the number

number=int(input('enter the number to be reversed '))
summation=0
while (number!=0):
    remainder=number%10
    summation=summation*10+remainder
    number=number//10

print('The reversed number is %d' %summation)    
