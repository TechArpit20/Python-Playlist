# Single Line Comment-
''' Double/Multi Line 
Comment    '''

'''
Data types are the categorization of data items. 
It represents the kind of value that tells what operations can be performed on a particular data.
Types of Datatypes-
1. Numeric  ---> integer, float, complex
2. Sequence Type ---> String, List, Tuple
3. Boolean
4. Set
5. Dictionary
'''
#Integer
a=5
print(a)
print(type(a))

#Float
b=5.0
print(b)
print(type(b))

# Complex number= a+bi
c=4+ 3j
print(c)
print(type(c))

#String
s="Arpit"
print(s)
print(type(s))

#list
li=list()
l2=[]
l3=['A','r','p',1]
print(li, l2, l3)
print(type(li),type(l2),type(l3))

#tuple
t1=tuple()
t2=()
t3=('A','r','p')
print(t1)
print(type(t1),type(t2),type(t3))

#Boolean
x=True
y=False
print(type(x), type(y))

#Set
s1=set()
s2={1,2,3}
print(s1)
print(type(s1),type(s2))

#Dictionary
d1=dict()
d2={}
d2={'Name':'Arpit'}
print(d1['Name'])
print(type(d1))