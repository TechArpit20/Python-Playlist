########### Identity  ################r#######
print('\nIdentity Operators')
a=[1,2,3]
b=[1,2,3]
c=a
d='Arpitsssssssssssssssss'
e='Arpitsssssssssssssssss'
f='Arpit Dadhich'
g=257
h=257

print(a is b)
print(a is c) ##Returns true because c is pointing to the same object
print(d is e)
print(d is f)  
print(g is h)
print(a is not e)

########### Membership  ################r#######
print('\nMembership Operators')
a='a'
b='abc'
c='arpit'
d='Arpit'
e='apt'
print(a in b)
print(a in c)
print(a in d)
print(d in a)
print(e in c)
print(e not in c)

########### Bitwise  ################r#######
print('\nBitwise Operators')
a=6 # 0110
b=4 # 0100

print('OR: ', a|b)  #    0110
print('AND: ', a&b)
print('XOR: ', a^b)
print('NOT: ', ~a)  # ~y=-y-1 => 0110 + 1= 0111
print('<<: ', a<<1) # 1100
print('<<: ', a<<2) # 0001 1000
print('<<: ', a<<3) # 0011 0000
print('>>: ', a>>1) # 0110
print('>>: ', a>>2) # 0011
print('>>: ', a>>3) # 0001