#关于slice

#跨步切片的语法和matlab不一样
s = 'bicycle'
s[::-2]
'eccb'

#1 seq.__getitem__(slice(start, stop, step))是切片的本质

labview_ad="""
0.....6.............20.........30.......40
hxh   male          175           basket
yzs   male          172           running
xcj   male          183           tennis
"""
labview_list=labview_ad.split('\n')[2:] #利用换行符将数据转成为数组，方便输出

#下面进行切片处理，首先利用slice()确定切片的模式

name=slice(0,6)
sex=slice(6,20)
height=slice(20,30)
love=slice(30,40)

for man in labview_list:
    print(man[name],man[height])

#2 python 内置的函数只能进行一维切片。其实可以用连续的索引代替
#Ellipsis的用法、

#Assigning to slices
a=list(range(10))
a[:5]=[10]
del a[3]
print(a)

a[::2]=['hxh','xcj','yzs']
print(a)

#3 Using + and * sequences
#这里面会出现很多的问题,list类型在赋值的时候传送的是地址，等式两边指向同一个地址，而tuple就不是这样
#mutable 和 immutable使用 +=，*=等符号时的区别，str也不同
#immutable在使用+=，*=时效率更低，因为运算过程中包含copy一步，str类型除外。

id([1,2,3])#查询地址

#tuple套 list会有神奇的现象
import dis
dis.dis('s[a]+=b')

t = (1, 2, [30, 40])
t[2] += [50, 60]
t

#4 sorting

#hahah

#haha1

#whats is wrong 


#fuckkkk you