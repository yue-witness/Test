# -*- coding: utf-8 -*-

import random
import time

# 对应关系
shu_to_gua = {1: '111', 2: '011', 3: '101', 4: '001', 5: '110', 6: '010', 7: '100', 8: '000'}
gua_to_ming = {'111': '乾', '011': '兑', '101': '离', '001': '震', '110': '巽', '010': '坎', '100': '艮', '000': '坤'}
yao_to_tu = {'1': '---', '0': '- -'}
gua_to_wuxing = {'111': '金', '011': '金', '101': '火', '001': '木', '110': '木', '010': '水', '100': '土', '000': '土'}

# 开头
print('This is a program simplify the calculation of MeiHuaYiShu ')
print('Please input two integer numbers, if you input 0 it will produce random numbers')

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
    shichen = (hour+3)/2

# 确定输入的数的卦
up = shu_to_gua[n1 % 8]
down = shu_to_gua[n2 % 8]
dongyao = (shichen+n1+n2) % 6
if dongyao<=3:
    ti = up
    yong = down


else:
    ti = down
    yong = up

shanghu = down[2]+up[0]+up[1]
xiahu = down[1]+down[2]+up[1]
bian = up

# 输出卦象
print('体    用    上    下    变')
for i in range(3):
    ti_tu = yao_to_tu[ti[i]]
    yong_tu = yao_to_tu[yong[i]]
    shanghu_tu = yao_to_tu[shanghu[i]]
    xiahu_tu = yao_to_tu[xiahu[i]]
    bian_tu = yao_to_tu[bian[i]]
    print(ti_tu, ' ', yong_tu, ' ', shanghu_tu, ' ', xiahu_tu, ' ', bian_tu)
ti_ming = gua_to_ming[ti]
yong_ming = gua_to_ming[yong]
shanghu_ming = gua_to_ming[shanghu]
xiahu_ming = gua_to_ming[xiahu]
bian_ming = gua_to_ming[bian]
print(ti_ming, '  ', yong_ming, '  ', shanghu_ming, '  ', xiahu_ming, '  ', bian_ming)

