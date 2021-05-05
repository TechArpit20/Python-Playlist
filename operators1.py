'''
Operatore are basically used to perform various operations on the values contained in different variables
Types of Operators:
1. Arithmetic operators=>  Addition(+), Subtraction(-), Multiplication(*), Division(/), Modulus(%), Exponential(**), Floor Division(//)
2. Assignment => (=), (+=), (-=), 
3. Comparison operators=> Equal(==), Not equal(!=), Greater than(>), Less than(<), Greater than and equal to(>=)
4. Logical operators=> and, or, not
5. Identity operators=> is, is not
6. Membership operators=> in, not in
7. Bitwise operators=> AND(&), OR(|), XOR(^), NOT(~), Zero fill Left Shift(<<), Signed Right Shift(>>)
'''
a=10
b=8

########### Arthmetic  ################r#######
print('\nArithmetic')
print('Addition: ',a+b)
print('Subtraction: ',a-b)
print('Mutliplication: ',a*b)
print('Division: ',a/b)
print('Modulus: ',a%b)
print('Exponential: ',a**b)
print('Floor Division: ',a//b)

########### Assignment  #######################
print('\nAssignment')
c=a
print('=: ',c)

c=10
c+=2  #c=c+2
print('+=: ',c)

c=10
c-=2
print('-=: ',c)

c=10
c*=2
print('*=: ',c)

c=10
c/=2
print('/=: ',c)

c=10
c**=2  # c= c**2
print('**=: ',c)

c=10
c//=2
print('//= ',c)

########### Comparison  #######################
print('\nComparison')
a=10
b=5
c=10
d=[1,2,3]
e=[1,2,3]
f=[1,2,3,4]

print(a==b)
print(a==c)
print(d==e)
print(d==f)
print(a!=b)
print(a<b)
print(a>c)
print(a>=c)
print(a<c)
print(a<=c)

########### Logical  #######################
print('\nLogical')
a=10
b=5
c=10
print(a==b and a==c)  # False and True => False
print(a==b or a==c)   # False and True => True
print(not(a==b))
print(not(a==b or a==c))











