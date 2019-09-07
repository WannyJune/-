#coding:utf-8
#作为库

class RotatedNum():
    def build(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
        return self
    def getPrint(self):
        print (self.num, self.x, self.y)

class RotatedArray():
    def __init__(self):
        self.array = []
    def appendNum(self, Num):
        self.array.append(Num)
        #print self.array[0].num
    def increaseArray(self, n):
        for Num in self.array:
            Num.num += 4*n+4
            Num.x += 1
            Num.y += 1
        #print self.array
        return self
    def combineArray(self, Array):
        #print bool(self.array)
        for Num in Array.array:
            self.appendNum(Num)
            #Num.getPrint()
        return self
        
class GetRotatedArray():
    def getSide(self):
        n = int(raw_input('input side:\n'))
        return n

        
    def getOutsideArray(self,n):
        Array = RotatedArray()
        if n == 1:
           Array.appendNum(RotatedNum().build(1, 0, 0))
           return Array
        for i in range((n-1)*4):
            Num = RotatedNum()
            num = i + 1
            mod = i%(n-1) #余
            quo = i/(n-1) #商
            if quo == 0:
                x = mod
                y = 0
                Num.build(num, x, y)
            elif quo == 1:
                x = n-1
                y = mod
                Num.build(num, x, y)
            elif quo == 2:
                x = (n-1)-mod
                y = n-1
                Num.build(num, x, y)
            elif quo == 3:
                x = 0
                y = (n-1)-mod
                Num.build(num, x, y)
            Array.appendNum(Num)
        return Array
        
    def getArrayBase(self, n):
        return self.getOutsideArray(n)
    
    def gen(self, n):
        if n == 1:
            return self.getArrayBase(1)
        elif n == 2:
            return self.getArrayBase(2)
        else:
            #print self.getOutsideArray(1).array
            insideArray = self.gen(n-2).increaseArray(n-2)
            #print insideArray.array
            outsideArray = self.getOutsideArray(n)
            #print outsideArray.array
            return insideArray.combineArray(outsideArray)
                
        



if __name__ == '__main__':
    #test
    #print a.x
    pass

    #tests = GetRotatedArray().getArray2().array
    #for test in tests:
        #print (test.num, test.x, test.y)
        
    
    GRA = GetRotatedArray()
    side = GRA.getSide()
    GPA2 = GRA.gen(side)
    
    for Num in GPA2.array:
        Num.getPrint()
    
    
    
    
    
    
    