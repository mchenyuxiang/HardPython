#-*-coding:utf-8-*-
import math

def is_sqr(x):
	return int(math.sqrt(x))*int(math.sqrt(x))==x

print filter(is_sqr,range(1,101))
