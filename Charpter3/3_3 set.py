#Set elements must be hashable. The set type is not hashable, but frozenset is, so you can have frozenset elements inside a set.

a=[1,1,2,3,4,5,6]
b=[2,3,9,33,4,5,2,3,1]
a_set=set(a)
b_set=set(b)

#两边都是set
c=a_set&b_set #找相同部分
found = len(set(a).intersection(b))
#任何可迭代变量都可以用set来进行并集交集运算，这种方法比直接使用list比较要快(在它们都已经是set的情况下)

d=a_set-b_set #剔除
len(c)

#创建set,利用{}创建会快一些。drozenset只能用 constructor来构造

a=set()#空set,不可用{}创建

#p83 p84 set的各种操作。
#set 的math操作，除了Infix类型的，都可以和任意iterable的进行运算 

#look up items 时，请务必使用dict或者set,这两个速度最快