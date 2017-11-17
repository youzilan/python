#coding=utf-8
import  xlrd

""" class iterator(object):
   def __init__(self):
        return self


    def __iter__(self):
        self.stop=13
        self.value=7

    def next(self):
        if self.value>=self.stop:
            raise  StopIteration
        self.value=self.value+1
        print self.value
        return self.value


numIterator=iterator()
print numIterator.next()

"""
class excleiter:

    def __init__(self, _start, _end):
        self.start = _start
        self.end = _end

    def get_next(self):
        s = self.start
        if(self.start < self.end):
            self.start += 1
        else:
            raise StopIteration

        return s


c = counter(1, 5)
iterator = iter(c.get_next, 3)
print(type(iterator))
for i in iterator:
    print(i)