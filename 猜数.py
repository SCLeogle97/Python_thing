import random
secret=random.randint(1,10)
print('chen hang')
temp=input("请输入一个数：")
guess=input(temp)
while guess !=secret:
    temp=input("wrong")
    guess=input(temp)
    if guess == secret:
        print("you got it")
    else:
        if guess> secret:
            print("big one")
        else:
            print("small one")
print("over")
