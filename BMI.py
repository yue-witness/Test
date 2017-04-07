# -*- coding: utf-8 -*-
#this program is calculate BMI

print('this program is calculate BMI')
height = float(input('please input your height\n'))
weight = float(input('please input your weight\n'))
bmi = weight/(height*height)

print('your BMI is ','%d' % bmi,'and you is ',end='')
if bmi<18.5:
	print('too light')
elif bmi<25:
	print('standard')
elif bmi<28:
	print('a little heavy')
elif bmi<32:
	print('heavy')
else: 
	print('too heavy')