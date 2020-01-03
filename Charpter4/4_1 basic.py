#1 Character issues

s = 'café'#人类可读的语句
b=s.encode('utf-8')#encode后 交给机器
len(s)
len(b)#5个字节，é占用两个字节，四个16进制字符
b.decode('utf8')
#2 Byte essentials

cafe=bytes('café',encoding='utf-8')
#直接索引会返回0-255
print(cafe[3])
print(cafe[4])
#slive会返回 bytes的切片
print(cafe[-1:])
print(cafe[3:5])

cafe_array=bytearray(cafe)

print(cafe_array[3])
print(cafe_array[4])
print(cafe_array[-1:])
print(cafe_array[3:5])

#bytes 将Ascii和 hexadecimal 相结合

#3 创建bytes的方法 bytes.fromhex()
#bytes.fromhex()
t=bytes.fromhex('49 f3 89')

#bytes(str,encoding=)

#a.encode('utf-8')

#iterable

a=bytes((i for i in range(15)))#注意这个输出的形式，并没有encoding. 和bytes(str,encoding=)的 情况是不一样的。
b=bytes([65])
c=bytes((i for i  in [65]))
#空bytes

a=bytes(5)

#copy of other bytes or bytes_buffer,这用方法一定是要copy

import array

t=array.array('l',(i for i in range(10)))
tt=array.array('b',(i for i in range(10)))
a=bytes(t)
b=bytes(tt)
print(a,'\n',b)

#4 memory view 控制bytee  share memory,structure
#memoryview和struct对bytes的处理很重要，需要另外参考p102下部和-103上部有说明