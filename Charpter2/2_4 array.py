#1 利用array代替可以节省内存，array内部元素的格式是指定的

import array
import random
import bisect

floats=array.array('d',(random.random() for i in range(10))) #双精度类型的array,第二个参数可以使任何可迭代形式
                                                             #random.random() :生成0-1的随机数

fp=open('floats_bin.bin','wb') #创建一个文件，模式为二进制写入。'wb':二进制写入，直接创建文件或清空数据在创建.
floats.tofile(fp)              #注意'w'和'wb', \r\n和 \n
fp.close()

floats_clone=array.array('d')#创建一个双精度array,接收数据

fp=open('floats_bin.bin','rb')
floats_clone.fromfile(fp,10)#需要确认写入个数

fp.close()

#pickle 也很fast,支持不同的数据类型。自定义的类型也支持。
#图像二进制存储方法
#table2-2记录了list和array的一些方法

#对array使用 sorted() 和 bisect.biect()、bisect.insort()

a=array.array('b',[2,2,3,4,5,5,6,3,7,2,6,39,6,0,2,5])
a=array.array(a.typecode,sorted(a)) #insort之前需要保证HACKSTACK已经被sorted了
bisect.insort(a,9)

#2 memoryview