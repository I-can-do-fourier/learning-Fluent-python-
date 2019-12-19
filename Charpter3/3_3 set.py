#Set elements must be hashable. The set type is not hashable, but frozenset is, so you can have frozenset elements inside a set.

a=[1,1,2,3,4,5,6]
b=[2,3,9,33,4,5,2,3,1]
a_set=set(a)
b_set=set(b)

#两边都是set
c=a_set&b_set #找相同部分
found = len(set(a).intersection(b))
d=a_set-b_set #剔除
len(c)

#创建set

a=set()#空set,不可用{}创建
