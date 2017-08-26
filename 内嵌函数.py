def fun1():
	print('123')
	def fun2():
		print('abc')
	fun2()

def Fun(x):
	def fun(y):
		return x * y
	return fun

def fun():
	x=[5]
	def fun1():
		x[0]*=x[0]
		return x[0]
	return fun1()    
