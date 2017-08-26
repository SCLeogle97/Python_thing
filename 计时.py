import time as t

class MyTimer():
    def _init_(self):
        self.unit=['年','月','日','小时','分钟','秒']
        self.prompt='未开始计时'
        self.lasted=[]
        self.begin=0
        self.end=0

    def _str_(self):
        return self.prompt

    _repr_=_str_

    def _add_(self,other):
        prompt="总共运行了"
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt+=(str(result[index])+self.unit[index])
        return prompt        
        
    
    def start(self):
        self.begin=t.localtime()
        self.prompt="请先调用stop（）"
        print('计时开始')

    def stop(self):
        if not self.begin:
            print('请先调用begin（）')
        else:    
            self.end=t.localtime()
            self._calc()
            print('计时结束')

    def _calc(self):
        self.lasted=[]
        self.prompt="总共运行了"
        for index in range(6):
            self.lasted.append(self.stop[index]-self.start[index])
            if self.lasted[index]:
                self.prompt+=str(self.lasted[index])

       
        self.begin=0
        self.end=0
