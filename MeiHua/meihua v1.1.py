# -*- coding: utf-8 -*-

import random
import time

# 对应关系
shu_to_gua = {1: '111', 2: '011', 3: '101', 4: '001', 5: '110', 6: '010', 7: '100', 0: '000'}
gua_to_shu = {'111': 1, '011': 2, '101': 3, '001': 4, '110': 5, '010': 6, '100': 7, '000': 0}
gua_to_ming = {'111': '乾', '011': '兑', '101': '离', '001': '震', '110': '巽', '010': '坎', '100': '艮', '000': '坤'}
gua_to_xiang = {'111': '天', '011': '泽', '101': '火', '001': '雷', '110': '风', '010': '水', '100': '山', '000': '地'}
yao_to_tu = {'1': '---', '0': '- -'}
gua_to_wuxing = {'111': '金', '011': '金', '101': '火', '001': '木', '110': '木', '010': '水', '100': '土', '000': '土'}
1
# 开头
print('This is a program simplify the calculation of MeiHuaYiShu ')
print('Please input two integer numbers, if you input 0 it will produce random numbers')

# 定义卦类
class liushisigua(object):
    def __init__(self, gua):
        self.gua = gua
    def tu(self, i):
        return yao_to_tu[self.gua[i]]

class bagua(liushisigua):
    def __init__(self, gua):
        self.gua = gua
        self.ming = gua_to_ming[gua]
        self.wuxing = gua_to_wuxing[gua]
        self.shu = gua_to_shu[gua]
        self.xiang = gua_to_xiang[gua]

# 输入两个数或者随机生成两个数
def equaltozero(x):
    if x == 0:
        return random.randint(1, 9999)
    else:
        return x
n1 = abs(int(input('The first number is ')))
n2 = abs(int(input('The second number is ')))
n1 = equaltozero(n1)
n2 = equaltozero(n2)

# 获取当前时间
localtime = time.localtime(time.time())
hour = localtime[3]
if (hour+3)/2 == 13:
    shichen = 1
else:
    shichen = int((hour+3)/2)

# 确定输入的数的卦与变卦
up = shu_to_gua[n1 % 8]
down = shu_to_gua[n2 % 8]
dongyao = (shichen+n1+n2) % 6


def zhuan(bianyao):
    if bianyao == '0':
        return '1'
    else:
        return '0'

if dongyao == 1:
    ti = up
    yong = down
    bian = down[0: 2]+zhuan(down[2])
elif dongyao == 2:
    ti = up
    yong = down
    bian = down[0]+zhuan(down[1])+down[2]
elif dongyao == 3:
    ti = up
    yong = down
    bian = zhuan(down[0]) + down[1: 3]
elif dongyao == 4:
    ti = down
    yong = up
    bian = up[0: 2]+zhuan(up[2])
elif dongyao == 5:
    ti = down
    yong = up
    bian = up[0]+zhuan(up[1])+up[2]
else:
    ti = down
    yong = up
    bian = zhuan(up[0])+up[1: 3]

zhugua = liushisigua(up+down)
if dongyao <=3 & dongyao >0:
    biangua = liushisigua(up+bian)
else:
    biangua = liushisigua(bian+down)

shanghu = bagua(up[1: 3]+down[0])
xiahu = bagua(up[2]+down[0: 2])
up = bagua(up)
down = bagua(down)
bian = bagua(bian)
ti = bagua(ti)
yong = bagua(yong)

# 输出体用互变
print('主    变')
for i in range(6):
    print(zhugua.tu(i), ' ',biangua.tu(i))
if dongyao <=3 & dongyao >0:
    print('体    用    上互  下    变')
else:
    print('体    用    上    下互  变')
for i in range(3):
    print(ti.tu(i), ' ', yong.tu(i), ' ', shanghu.tu(i), ' ', xiahu.tu(i), ' ', bian.tu(i))
print(ti.ming, '  ', yong.ming, '  ', shanghu.ming, '  ', xiahu.ming, '  ', bian.ming)
print(ti.wuxing, '  ', yong.wuxing, '  ', shanghu.wuxing, '  ', xiahu.wuxing, '  ', bian.wuxing)
