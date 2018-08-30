# -*- coding: utf-8 -*-
'''@author: Rayment
   @version: 1.0
   @note: 实现扫雷游戏(2011-9-20)
          测试环境:python2.5.2
'''
import sys
import random
import string

class MineSweeping():
    '''扫雷主程序
    '''

    def __init__(self):
        '''初始化函式
        '''
       
        self.ROW = 8
        self.LINE = 8
        self.SCORE = 0 #扫雷得分
        self.MineNum = 15 #地雷总数
        self.xy_list= [[0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0]]
       
       
    def iniData(self):
        '''x,y坐标初始状态值函数
           0-没有地雷;1-有地雷
        '''
       
        #游戏开始前所有数值归零
        for l in range(self.LINE):
            for r in range(self.ROW):
                self.xy_list[l][r]= 0
       
        Max = self.MineNum
        for x in range(self.LINE):
            for y in range(self.ROW):
                if 0 > Max:
                    self.xy_list[x][y]= 0
                else:
                    #为了增加地雷分布范围,选择0到4随机数
                    if 1 == random.randint(0,4):
                        self.xy_list[x][y]= 1
                        Max = Max - 1
                       
   
    def getX(self):
        '''获得x坐标值
           @return : 返回x坐标值
           @type : int
        '''
        sys.stdout.write('X=')
        xRet = input()
        while xRet=='' or (False == self.isNumber(xRet))\
             or 0>int(xRet) or int(xRet)>self.ROW -1:
            print('Wrong number!(please input 0-7)')
            sys.stdout.write('X=')
            xRet = input()
        return int(xRet)
       
       
    def getY(self):
        '''获得y坐标值
           @return : 返回y坐标值
           @type : int
        '''
        sys.stdout.write('Y=')
        yRet = input()
        while yRet=='' or (False == self.isNumber(yRet))\
             or 0>int(yRet) or int(yRet)>self.LINE -1:
            print('Wrong number!(please input 0-7)')
            sys.stdout.write('Y=')
            yRet = input()
        return int(yRet)
   
   
    def isNumber(self,strVal):
        '''检查是否数值
           @param : 需检查的字符串
           @type : str
        '''
       
        nums = string.digits
        for i in strVal:
            if i not in nums:
                return False
        return True
   

    def checkMine(self,xPos,yPos):
        '''检查输入坐标是否有雷
           0-没有地雷;1-有地雷;2-已经清扫
           @param 1: x坐标
           @type : int
           @param 2: y坐标
           @type : int
           @return : 0-没有地雷;1-有地雷;2-已经清扫
           @rtype : int
        '''
        if 0 == self.xy_list[xPos][yPos]:
            self.xy_list[xPos][yPos] = 2
            return 0
        elif 2 == self.xy_list[xPos][yPos]:
            return 2
        else:
            return 1
       
               
    def play(self):
        '''游戏运行函数
        '''
        self.display(1)
        self.SCORE = 0
        self.iniData()
        #print self.xy_list
        while(1):
            x = self.getX()
            y = self.getY()
            while(2 == self.checkMine(x,y)):
                print('values of x,y had inputed,please input new values!')
                x = self.getX()
                y = self.getY()
            if 1 == self.checkMine(x,y):
                self.end()
                break
            else:
                self.display(2)
                self.SCORE = self.SCORE + 1
               
           
    def end(self):
        '''游戏结束函数
        '''
       
        self.display(3)
        print('+======================+')
        print('+      Game Over       +')
        print('+======================+')
        print('   Your score is: %d    '%(self.SCORE))
       

    def display(self,kind):
        '''图形输出函数
           @param:1-初始;2-运行;3-结束
           @type:int
        '''
        if kind==1:
            print('+======================+')
            print('+      Game Start      +')
            print('+======================+')
            print('*-----------------*')
            for i in range(self.LINE):
                print('|', end = ' ')
                for k in range(self.ROW):
                    print('口', end = ' ')
                print('|')
            print('*-----------------*')
            print('Please input values of x,y(0-7):')
        elif kind==2:
            #输出已经清扫位置
            print('*-----------------*')
            for i in range(self.LINE):
                print('|', end = ' ')
                for k in range(self.ROW):
                    if 2 == self.xy_list[i][k]:
                        count = self.getCount(i,k)
                        print(count, end = ' ')
                    else:
                        print('口', end = ' ')
                print('|')
            print('*-----------------*')
            print('Please input values of x,y(0-7):')          
        else:
            #输出所有的地雷与已经清扫位置
            print('*-----------------*')
            for i in range(self.LINE):
                print('|', end = ' ')
                for k in range(self.ROW):
                    if 2 == self.xy_list[i][k]:
                        count = self.getCount(i,k)
                        print(count, end = ' ')
                    elif 1== self.xy_list[i][k]:
                        print('X', end = ' ')
                    else:
                        print('口', end = ' ')
                print('|')
            print('*-----------------*')
    def getCount(self,n,m):
        count = 0
        if n == 0:
            line = [n, n+1]
        elif n == (self.LINE - 1):
            line = [n-1, n]
        else:
            line = [n-1, n, n+1]
        if m == 0:
            row = [m, m+1]
        elif m == (self.ROW - 1):
            row = [m-1, m]
        else:
            row = [m-1, m, m+1]
        for i in line:
            for k in row:
                if 1 == self.xy_list[i][k]:
                    count += 1
        return count

           
       

if __name__ == '__main__':
    '''自测试
    '''
    ms = MineSweeping()
    while(1):
        ms.play()
        print('\n----------------------------------------------')
        print('Quit game press \'q\',otherwise press other key!')
        print('----------------------------------------------')
        inputVal = input()
        if 'q' == inputVal:
            break
