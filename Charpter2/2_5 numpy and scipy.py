import numpy as np
 #NumPy and SciPy

a=np.arange(10)
a.shape=2,5
print(a[:,3])  #numpy是可以直接进行二维索引的
np.shape(a)
b=a.transpose()
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