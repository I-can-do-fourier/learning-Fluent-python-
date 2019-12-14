#1 利用array代替可以节省内存，array内部元素的格式是指定的

import array
import random
import bisect
import numpy as np

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

#2 memoryview，不需要直接copy.直接修改memory

memtest=array.array('h',[-2,3,4,0,2,1,5])#signed 16bit int
memv=memoryview(memtest) #创建memoryview对象，方便进行memory分析。

memv_B=memv.cast('B')#将memoryview对象投射成unsigned 8bit int形式...其实变成signed 8bit int('b')也是可以的(操作上可以，实际上数据会有变化)
memv_Blist=list(memv_B)#变变为list显示出来//  memv_B。tolist()也可
memv_B[7]=4#这个地方不要用memv_Blist
print(memtest)  #多种对象全都指向同一个 memory,但是memory生成list是单独的，并不指向那个memory

#3 NumPy and SciPy

a=np.arange(10)
a.shape=2,5
print(a[:,3])  #numpy是可以直接进行二维索引的
np.shape(a)
b=a.transpose()#创建新的矩阵
print(a,'\n\n',b)

#高分辨率计算代码运行时长

from time import perf_counter as pc
import random

a=np.random.rand(1000000)
np.savetxt('D:\\ni',a)
b=np.loadtxt('D:\\ni')
np.save('D:\\nii',b)
c=np.load('D:\\nii.npy','r+')#注意这个读取模式,使用save和Load读写速度明显加快

t0=pc();a=3;a/=3;print(pc()-t0)