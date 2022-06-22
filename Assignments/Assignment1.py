#Numbers: Stored numerical info
#Strings: ordered sequence of characters
#Tuples: Order sequnce of objects
#Dictionary: Key-value printing that is unordered

from cmath import sqrt


print((2*50)+0.25)

print(4*(6+5))
print(4*6+5)
print(4+6*5)

#Floating Numbers

print(sqrt(16))
print(4**2)

s = 'hello'
print(s[1:2])
print(s[::-1])

print(s[-1])
print(s[4])

list1 = [0,0]
list1.append(0)
print(list1)

list2 = [0,0,0,0]
list2.pop(0)
print(list2)

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)


d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d =  {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#Tuples are immutable whereas lists are mutable
#We can create tuple by ()

#In a set there is only 1 unique rep. for each character

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

print(2>3)
print(3<=2)
print(3==2.0)
print(3.0==3)
print(4**0.5 !=2)


l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

#l_one[2][0] = 3
#l_two[2]['k1']= 4

l1 = l_one[2][0]
l2 = l_two[2]['k1']

print(l1 >= l2)





