f=lambda x:x*x
#f(1)

g=lambda x,y:x+y
#g(1,2)

#过滤器
list(filter(None,[1,0,False,True]))

def odd(x):
	return x%2
temp=range(10)
show=filter(odd,temp)
list(show)

