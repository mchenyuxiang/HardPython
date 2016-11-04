# -*- coding:utf-8 -*-
s = 'Python was started in 1989 by \"Guido\".\nPython is free and wasy to learn.'
print s


print r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.'''

print u'''静夜思

床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
'''


L=['Adam','Lisa','Paul','Bart']
L.pop(2)
L.pop(2)
print L


sum = 0
x = 1
n = 1
while True:
    sum += x
    n = n +1 
    if n > 20:
        break
    x = x * 2
print sum
