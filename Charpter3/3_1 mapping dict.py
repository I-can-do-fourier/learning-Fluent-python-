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

#setdefault

import sys
import re

WORD_RE = re.compile('\w+')