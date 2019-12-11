#基本sequences的用法

#Container Sequences:存储的是对象的引用，不开辟新的空间存储原数据
#Flat Sequences:开辟单独的内存放置数据，因此数据类型只有一种
#Mutable sequences:可变的序列
#Immutable sequences:不可变得序列 
#Keeping in mind these common traits — mutable versus immutable; container versus flat — is helpful to extrapolate what you know about one sequence type to others

#以下是List comprehensions and generators expressions

#1 listcomp和 map+filter，速度测试：https://github.com/fluentpython/example-code/blob/master/02-array-seq/listcomp_speed.py
 
colors=['black','white']
sizes=['S','M','L']

tshirts1=[(c,s) for c in colors for s in sizes]
tshirts2=[(c,s) for s in sizes for c in colors]

#2Generator expressions

symbols='129jeff32$%'

tuple(ord(symbol) for symbol in symbols)#生成器可以不加额外的括号

import array

array.array('I',(ord(symbol) for symbol in symbols))#此时生成器的括号是必需的

#利用generator 一次一个输出tuple,不过多占用内存
colors=['black','white']
sizes=['S','M','L']

for tshirt in ('%s %s'%(color,size) for color in colors for size in sizes):
    #注意：%s和%r 的区别
    print(tshirt)

#3Tuples的作用。Field，number,order。sorted()会distroy tuple
#tuple每个元素的位置就是这个元素的名字
#尝试以下两句话
print('%s/%s'%[1,2])
print('%s/%s'%([1,2],3))
#tuple 最重要的功能就是unpacking

t=(20,8)
quotient,remainder=divmod(*t)#类似于一种自定义的unpacking
_,filename = os.path.split('/home/luciano/.ssh/idrsa.pub')#原理同上

# *的用法
#4 nested tuple unpacking

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15s}|{:^20s}|{:^20s}'.format('','lat.','long.'))
fmt='{:15s}|{:^20.6f}|{:^20.6f}'
for city,ab,cc,(latitude,longtitude) in metro_areas:
    if longtitude<0:
        print(fmt.format(city,latitude,longtitude))

#named tuple
 
import collections

#第一种创建方法
City=collections.namedtuple('Cities','name country population coordinates')
tokyo=City('Tokyo','Japan','36.933',(35.689722,139.691667))

#第二种创建方法
City._fields #查看都有那些参数

delhi_para=('Delhi','IN',21.935,(28.613889,77.208889)) #包含所有参数的tuple
delhi=City._make(delhi_para)
delhi._asdict() #显示所有数据,方便数据的迭代显示

#第三种方法，将坐标也变成一个namedtuple

coordin=collections.namedtuple('coordinates','lat long')
delhi_coordin=coordin(28.613889,77.208889)
delhi_para=('Delhi','IN',21.935,delhi_coordin)
delhi=City._make(delhi_para)
delhi._asdict() 