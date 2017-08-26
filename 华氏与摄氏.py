class Celsius:
    def _init_(self,value=26.0):
        self.value=float(value)

    def _get_(self,instance,owner):
        return self.value

    def _set_(self,instance,value):
        self.value=float(value)

class Fahrenheit:
    def _get_(self,instance,owner):
        return instance.cel*1.8+32

    def _set_(self,instance,value):
        instance.cel=(float(value)-32)/1.8
    
class Temp:
    cel = Celsius()
    fah=Fahrenheit()
