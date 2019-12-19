# hashble的概念，保证每个元素都是 immutable
#1 生成dict

a=dict(one=1,two=2,three=3)
b={'two':2,'one':1,'three':3}
c=dict(zip(['one','two','three'],[1,2,3]))
d=dict([('two',2),('one',1),('three',3)])
e=dict({'three':3,'two':2,'one':1})
f=dict(**{'three':3,'two':2,'one':1})

a==b==c==d==e==d

#dict comprehensions,可以用类似listcomp,genexps的表达生成dict

people=[('hxh',175),('yzs',172),('xcj',183)]

people_dict={name.upper():height for name,height in people}

print(people_dict)

#2 mapping类型的一般概括
# mapping的methods 见 p67  dict defaultdict  ordereddict

dict.update

#3 setdefault

import sys
import re
import collections

WORD_RE = re.compile('\w+') #相当于一个扫描的过程

word_index={}

with open('C:\\Users\\hanxinhang\\Desktop\\learning-Fluent-python-\\Charpter3\\test.txt',encoding='utf-8') as fp:
    for line_num,line in enumerate(fp,1):#利用此语句得到的索引是针对字母的，且包含空格。要想真正所引出单词的位置，需要用另一种迭代方法
        for gener in WORD_RE.finditer(line):
            location_x=gener.start()+1
            word=gener.group()
            word_index.setdefault(word,[]).append((line_num,location_x))#这句话可以用 dict.get()等相对的复杂的过程代替

for word in sorted(word_index, key=str.upper):
    print(word, word_index[word])


"""
with open('C:\\Users\\hanxinhang\\Desktop\\learning-Fluent-python-\\Charpter3\\test.txt',encoding='utf-8') as fp:
    for line_num,line in enumerate(fp,1):#利用此语句得到的索引是针对字母的，且包含空格。要想真正所引出单词的位置，需要用另一种迭代方法
        for num,word in enumerate(WORD_RE.finditer(line)):
            word=word.group()
            word_index.setdefault(word,[]).append((line_num,num+1))

for word in sorted(word_index, key=str.upper):
    print(word, word_index[word])

"""


#4 defaultdict  实际上是在dict中封装了一个__missing__ method. 当使用__getitem__ method(对应dd[k])时，若缺乏key, __missing__ method 会被唤醒。

index=collections.defaultdict(int)

with open('C:\\Users\\hanxinhang\\Desktop\\learning-Fluent-python-\\Charpter3\\test.txt',encoding='utf-8') as fp:
    for line_num,line in enumerate(fp,1):#利用此语句得到的索引是针对字母的，且包含空格。要想真正所引出单词的位置，需要用另一种迭代方法
        for gener in WORD_RE.finditer(line):
            location_x=gener.start()+1
            word=gener.group()
            index[word].append((line_num,location_x))#这句话可以用 dict.get()等相对的复杂的过程代替

for word in sorted(word_index, key=str.upper):
    print(word, word_index[word])

#注意__getitem__,dd[k],dd.get()之间的区别

## StrKeyDict0 converts it to str when it is not found

class StrKeyDict0(dict):

    def __missing__(self,key):
        if isinstance(key,str):     #避免程序无限次执行
            raise KeyError(key)                     #注意抓住一个物质的特点，不要只从大方面考虑.这里是raise
        key=str(key)
        
        return self[key]
    
    def get(self,key,default_return=None):     #为了能让get方法也能调用__missing__ method  get方法要是key没有找到，不会报错. 因此用try....except
        try:
            return self[key]
        except KeyError:
            return default_return 
    
    def __contains__(self,key):
        return key in self.keys() or str(key) in self.keys() #此处不能用 key in self,否则会发生死循环。
        #这种表达形式其实是一种view,这样的速度比单纯扫描list要快

    
            
