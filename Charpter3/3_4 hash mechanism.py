#1 hash的机理

#hash 如何影响dict

#自定义的类都是 hashable的
#如果自定义类中定义了__eq__,那么一定要再定义一个__hash__

a=(1,2,3)
b=(1,2,3)
a==b
hash(a)==hash(b)

# modifying the contents of a dict while iterating through it is a bad idea.因为修改的过程中hash table会改变