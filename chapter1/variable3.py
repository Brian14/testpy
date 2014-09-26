__author__ = 'BAOBR'

cars = 100.0
drivers = 30
# test
# print("this is  ", cars + drivers + test, " :end")

# 浮点数的问题
print(0.1 + 0.2 + 0.1 + 0.2)

name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print("let's talk about %s." % name)
print("he's %d inches tall" % height)
print("he's %d pounds heavy" % weight)

# %后面的参数个数需要和前面的格式化字段里的一致
print("he's %d pounds heavy, and eys is %s" % (weight, eyes))

#类型不符，不能强转
#print("if i add %d, %d, and %d, i get %d" % (age, height, weight, eyes + height + weight))

