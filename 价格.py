def discount(price,rate):
    f_p=price*rate
    print('这里试图打印全局变量的值：',o_p)
    o_p=50
    print('修改后值为:',o_p)
    return f_p

o_p=float(input('请输入原价:'))
rate=float(input('请输入折扣率:'))
n_p=discount(o_p,rate)
print('修改后值为:',o_p)
print('打折后价格为：',n_p)
