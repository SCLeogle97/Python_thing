#方式1
def fac(n):
	result=n
	for i in range(1,n):
		result*=i
	return result

no=int(input('请输入正整数：'))
result=fac(no)
print('%d的阶乘是：%d'%(no,result))

#方式2
def fac(n):
    if n==1:
        return 1;
    else:
        return n*fac(n-1)
n=int(input('请输入一个数：'))
result=fac(n)
print('%d的阶乘是：%d'%(n,result))
