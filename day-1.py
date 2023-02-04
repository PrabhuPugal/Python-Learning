print("Hello")
print("69 is the position")


# list

l=[12,321]
l.append(23)
l.remove(23)
l.pop(0)
l.insert(3,43)
l.extend([132,31])
l[:2]

# tuple

t=(1,2,4)
t.count(2)
a,b=(3,4) # unpacking of tuple

# set

# s=set()
s={12,3,4}
s.add(2)
print(s)
s.remove(2)
s.update([2,4,1,2])
s.update((5,6,7,7))
s.update({10,32,11})
print(s)

# dict

d={'a':[12,12,1],'b':(1,2,4,2),'c':{12,13,12,3},'d':{'a':12,'b':21}}
# d['a']=12
print(d)
d['a']=12
print(d)
del d['a']
print(d)

print(d['d'].keys())  #('a','b','c','d')
print(d.values())
print(d.items())
print(type(d.values()))

# key - string, tuple, num

print(len(d))

# 1...10

l=[x for x in range(10) if x%2==0] # list comprehension
print(l)

# l.sort() 
# l1=l.sorted()

# l2=l1.copy()

# l2=l1
a=[10,20]
b=a
b+=[30,40] #append
print(a)
a+=[1,2,3]
print(b)

l=list({1,2,4})
print(l)
l=list((1,2,4))
print(l)

s=set([1,2,3,4])
print(s)

s=set({'a':2,'b':3})
print(s)

s="a is {}, b is {}".format(a,b)
s=f'a is {a} '

a=8//3 # floor division
# a=2