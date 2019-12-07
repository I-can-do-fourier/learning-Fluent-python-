import collections

Card=collections.namedtuple('Card',['rnak','suits'])

class FrenchDeck:
    rank=[str(i) for i in range(2,11)]+list('JQKA')
    suits="spades diamonds clubs hearts".split()
    suits2=["haha","haha","haha","haha","haha","haha","haha","haha"]
    def __init__(self):
        self.cards=[Card(m,n) for m in self.rank for n in self.suits]
        #self.cards2=[Card(m,n) for m in self.rank for n in self.suits2]
    def __len__(self):
        return len(self.cards)-3 #注意这个地方,这说明len()指令直接跳转到这个method
    
    def __getitem__(self,key):
        return self.cards[key]
    def __pick__(self):
        return self.cards[1:5]
    
#region
#slice,iteration,reverse,dort,(shuffle???,待定)
#__iter__()和__getitem__()

