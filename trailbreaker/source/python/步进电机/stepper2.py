# 简单的单四拍模式
# main.py -- put your code here!
import pyb
from pyb import Pin

x1=Pin('X2',Pin.OUT_PP)
x2=Pin('X1',Pin.OUT_PP)
x3=Pin('X3',Pin.OUT_PP)
x4=Pin('X4',Pin.OUT_PP)
while True:
	x1.value(0)
	x2.value(1)
	x3.value(1)
	x4.value(1)
	pyb.delay(3)
	
	x1.value(1)
	x2.value(0)
	x3.value(1)
	x4.value(1)
	pyb.delay(3)
	
	x1.value(1)
	x2.value(1)
	x3.value(0)
	x4.value(1)
	pyb.delay(3)
	
	x1.value(1)
	x2.value(1)
	x3.value(1)
	x4.value(0)
	pyb.delay(3)