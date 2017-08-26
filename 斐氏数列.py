class Fibs:
	def _init_(self,n=10):
		self.a=0
		self.b=1
		self.n=n
	def _iter_(self):
		return self
	def _next_(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>self.n:
                    raise StopIteration
		return self.a
