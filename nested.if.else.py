#Neated if else


username=input('enter student name ')


if (username=='cse'):
    password=input('enter password ')
     
    if (password=='AEC'):
        print('valid student')
    elif (password!='AEC') :
        print('password incorrect')
else :
    print('username incorrect')
