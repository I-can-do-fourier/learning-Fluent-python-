#1 variations of dicts

#2 UserDict 用于创建子类。方便用户自定义类 避免了死循环等问题 ,保证存储的key均为str类型P76

import collections

class StrKeyDict(collections.UserDict):

    def __missing__(self,key):
        if isinstance(key,str):
            raise KeyError
        
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)]=item  #注意，这里是self.data.避免死循环 self.data的类型是dict,而self不是
                                  #普通的dict,没有dict.data，因此，不能将key强制转换成str

#3 immutable mappings     MappingProxyType      p78 可用于引脚封装等

        