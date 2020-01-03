
s1='cafe\u0301'
s2='café'
print(s1+'\n'+s2)
len(s1)==len(s2)

#1 unicodedata 
from unicodedata import normalize, name

print(len(normalize('NFC',s1))==s2.__len__())
print(len(normalize('NFD',s2))==s1.__len__())


#Some single characters are normalized by NFC into another single character.看起来一样，但是名字不一样 
ohm = '\u2126'

ohm_c=normalize('NFC',ohm)

print(len(ohm)==len(ohm_c))

print(ohm==ohm_c)

print(normalize('NFC',ohm)==ohm_c)

#NFKC and NFKD normalization should be applied with care and only in special cases — e.g. search and indexing
#and not for per‐manent storage, as these transformations cause data loss

#case folding 大多数情况下与 s.lower() 一样。。一小部分会有所不同，如