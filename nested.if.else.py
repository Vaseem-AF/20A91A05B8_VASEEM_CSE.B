#Nested if else


username=input('enter student name ')


if (username=='cse'):
    password=input('enter password ')
     
    if (password=='AEC'):
        print('valid student')
    elif (password!='AEC') :
        print('password incorrect')
else :
    print('username incorrect')

    #outputs :
enter student name cSe
username incorrect
    
enter student name cse
enter password aec
password incorrect
    
enter student name cse
enter password AEC
valid student    

