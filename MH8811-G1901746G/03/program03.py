"totally 3 sub-programs, enter 01 for hello world, enter 02 for hello someone, enter 03 for Celsius, enter exit for quit"

def greet(lang) :
    if lang == '01' :
        return 'Hello world' 
    elif lang== '02':
        nam= input('who are you')
        return 'hello,'+nam
    elif lang=='03': 
        c=float(input("input the Celsius!"))
        F=c*1.8+32
        return F
    else :
        return'no such choice'
while True:
    a=input('I have three sub-programs to share with you print 1 for hello word print 2 for hello someone print 3 for Celsius')
    if a=='exit':
        print('thank you bye!')
        break
    print (greet(a))

