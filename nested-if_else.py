print('###############  If Else ###########################################')
a=4
b=4
c=5

if a<b:
    print('a is less than b')
elif a==b:
    print('a is equal to b')
elif c>100:
    print('c is greater than 100')
else:
    print('b is greater than a')

if c<5:
    print('c is less than 5')

print('############### Nested If Else ###########################################')

str1='I like you'
str2='She likes you'
#str3='She likes you but she have a boyfriend'
str3=''

if str2=='She likes you':
    print('I need some more time')
    if str3:
        print('I like you but I have a bf')
    else:
        print('Immediate yes')
else:
    print('Blocked!!!!!!!!!!')

