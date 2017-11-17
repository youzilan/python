class animal(object):
    def run(self):
        print "animal is run"

class dog(animal):#animal:基类（父类），dog;子类
    pass           #子类继承父类的方法run()
ss
class cat(animal):
    pass

dog1=dog()
dog1.run()