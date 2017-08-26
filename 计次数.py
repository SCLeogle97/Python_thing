class Countlist:
    def _init_(self,*args):
        self.value=[x for x in args]
        self.count={}.fromkeys(range(len(self.values)),0)

    def _len_(self):
        return len(self.values)

    def _getitem_(self,key):
        self.count[key]+=1
        return self.values[key]
