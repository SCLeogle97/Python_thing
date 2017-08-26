class Rec:
	def _init_(self,x,y):
		self.x=x
		self.y=y
	def getper(self):
		return(self.x+self.y)*2
	def getarea(self):
		return self.x*self.y

class CapStr(str):
	def _new_(cls,string):
		string=string.upper()
		return str._new_(cls,string)

class c:
	def _init_(self):
		print ('abc')
	def _del_(self):
		print ('123')	    
