class New_int(int):
	def _add_(self,other):
		return int._add_(self,other)
	def _sub_(self,other):
		return int._sub_(self,other)

class Try_init(int):
	def _add_(self,other):
		return int(self)+int(other)
	def _sub_(self,other):
		return int(self)-int(other)    
