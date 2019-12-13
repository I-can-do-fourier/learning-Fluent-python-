#1 list.sort不会返回一个新的list，直接在原有List上修改。因此返回一个none

#sorted(list,key,reverse),key也应用在一些其他的函数之中
#注意sorted 的保序性

#比较sorted() 和 list.sort的区别

#2 bisect的用法，bisect.bisect() 和bisect.insort()
#一个简便的用法http://code.activestate.com/recipes/577197-sortedcollection/

#简化版的bisect.bisect演示，具体以example为准。

import bisect
import sys

HAYSTACK=[1,2,3,7,4,43,7,3,4,6,7,5,7,15,98,456,33,7]

NEEDLES=[2,4,5,6,7,2,34,89,4,4,222,64,76]
NEEDLES.sort()
HAYSTACK.sort()

show_fmt='num {:3d} | position {:3d} :{}'

def neversay(bisect_fn):

    for needle in reversed(NEEDLES):
        position=bisect_fn(HAYSTACK,needle)#显然，bisect.bisect(a,b)返回一个插入的位置
        seat=position*'   *'+''+str(needle)
        para=(needle,position,seat)
        print(show_fmt.format(*para))
        


if __name__=='__main__':
    title='HAYSTACK_SORT --------> ' +''.join('%4d' %i for i in HAYSTACK)  #这个join很有用
    print(title)
    neversay(bisect.bisect)

#3 利用bisect这种穿针的特性，可以实现分类、查表的功能

#4 bisect.insort()的用法
import random

Round=10
random.seed(12)#这个东东这里好像没有起到什么作用
output=[]
for i in range(Round):
    item=random.randrange(3+i) #给定生成随机数的范围和步长。但是有一点小问题，只输入一个参数时，相当于给定高的边界。
    bisect.insort(output,item)#bisect.insort()的返回值为none
    print('{:2d}----'.format(item),output)