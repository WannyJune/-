#coding=utf8
from math import sqrt

#这是一个尝试生成螺旋数列的练习程序，
#使用递归的规律，即
#一个螺旋数列是由最外层和内层部分组成
#而内层部分又由外层部分和内层部分组成
#最终最里面可以表示为1+n的平方（奇数）
#或1,2,3,4各项与n的平方的加和

#大致是这样吧

#定义 螺旋数 类
class LuoXuanShu():
    def build(self, xuShu, xpos, ypos):
        self.xuShu = xuShu
        self.xpos = xpos
        self.ypos = ypos
        #以第一个数为坐标（1,1）以向右为X轴正方向，以向下为Y轴正方向，建立坐标系
        return self



#操作螺旋数列的类，包含一些操作螺旋数列的方法
class OperateLuoXuanShuLie():
    #生成最外层螺旋数列,n是最外层边数
    def genZuiWaiCengLuoXuanShuLie(self, n):
        #print n#
        outestShuLie = []
        for xuShu in range(1,4*n-3):
            shang = xuShu/(n-1)#求序数除以n-1的商
            yuShu = xuShu%(n-1)#求序数除以n-1的余
            #分余数为零和非零的情况，余数为零则要把余数补成满
            if yuShu == 0:
                groupNum = shang
                posInGroup = n-1
            else:
                groupNum = shang+1
                posInGroup = yuShu
            #直接将序数的商和余数 与 坐标对应
            if groupNum ==1:
                zuoBiao = (posInGroup,1)
            elif groupNum == 2:
                zuoBiao = (n,posInGroup)
            elif groupNum ==3:
                zuoBiao = (n+1-posInGroup,n)
            elif groupNum == 4:
                zuoBiao = (1,n+1-posInGroup)
            #将得到的坐标与螺旋数序数对应并添加到输出列表中，并返回该列表
            luoXuanShu = LuoXuanShu().build(xuShu,zuoBiao[0],zuoBiao[1])
            outestShuLie.append(luoXuanShu)
        return outestShuLie
    #得到基本数列，螺旋数列1和螺旋数列2
    def getBasicLuoXuanShuLie(self,bianShu):
        if bianShu == 1:
            return [LuoXuanShu().build(1,1,1)]
        elif bianShu == 2:
            return self.genZuiWaiCengLuoXuanShuLie(2)
    #使螺旋数列自增，包括位置和序数
    def ziZeng(self,luoXuanShuLie):
        for luoXuanShu in luoXuanShuLie:
            d = (sqrt(len(luoXuanShuLie))+1)*4
            luoXuanShu.xuShu +=  int(d)
            luoXuanShu.xpos += 1
            luoXuanShu.ypos += 1
        return luoXuanShuLie
    #得到螺旋数列
    def genLuoXuanShuLie(self,bianShu):
        if bianShu > 2:
            oldLuoXuanShuLie = self.genLuoXuanShuLie(bianShu-2)
            updatedLuoXuanShuLie = self.ziZeng(oldLuoXuanShuLie)
            outerLuoXuanShuLie = self.genZuiWaiCengLuoXuanShuLie(bianShu)
            outputLuoXuanShuLie = outerLuoXuanShuLie + updatedLuoXuanShuLie
            return outputLuoXuanShuLie
        elif bianShu == 2 or bianShu ==1:
            return self.getBasicLuoXuanShuLie(bianShu)
            




#打印螺旋数列的类
class PrintLuoXuanShuLie():
    #打印螺旋数列通过控制台
    def printLuoXuanShuLie(self,inputLuoXuanShuLie):
        n = int(sqrt(len(inputLuoXuanShuLie)))
        output = []
        maxLuoXuanShu = 0
        for heng in range(n):
            output.append([])
            for zong in range(n):
                output[heng].append(None)
        for luoXuanShu in inputLuoXuanShuLie:
            output[luoXuanShu.ypos-1][luoXuanShu.xpos-1]=luoXuanShu.xuShu
            if luoXuanShu.xuShu > maxLuoXuanShu:
                maxLuoXuanShu = luoXuanShu.xuShu
        for line in output:
            line_str = ''
            for num in line:
                bit = len(str(maxLuoXuanShu))
                
                num = (bit-len(str(num)))*' '+str(num) if len(str(num)) < bit else num
                line_str = line_str + str(num) + ' '
            print line_str

        


if __name__ == '__main__':
    pass
    #test
    #testLuoXuanShu = LuoXuanShu().build(1,1,1)
    #print testLuoXuanShu
    #print testLuoXuanShu.xpos
    #测试螺旋数类使用，成功

    #test
    #i = 4
    #nn = 3
    test = OperateLuoXuanShuLie()
    #outesttest = test.genZuiWaiCengLuoXuanShuLie(nn)
    #print test[i-1].xuShu,test[i-1].xpos,test[i-1].ypos
    #test success

    #basic2 = test.getBasicLuoXuanShuLie(2)
    #print basic2[i-1].xuShu,basic2[i-1].xpos,basic2[i-1].ypos#
    #test success
    #PrintLuoXuanShuLie().printLuoXuanShu(ookoooo)
    #PrintLuoXuanShuLie().printLuoXuanShu(outesttest)
    #print outesttest[-1].xuShu
    #finally test success!!!!!!
    while True:
        try:
            inputInform = input("输入边数：")
        except:
            continue
        if inputInform==0:
            exit()
        elif type(inputInform) == int:
            zhengShiTest = test.genLuoXuanShuLie(inputInform)
            PrintLuoXuanShuLie().printLuoXuanShuLie(zhengShiTest)

    
