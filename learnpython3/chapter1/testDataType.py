__author__ = 'BAOBR'

var = -97

s = ("s1", "s2", "s3")
t = {"s1", "s2", "s3"}
w = ["s1", "s2", "s3"]
print(type(s))
print(type(t))
print(type(w))

input1 = input("please input something")
p = s

print(len(s))
print(len(t))
print(len(w))

w.append("ssr")

print(w)

print(s is t)
print(input1)

if "":
    print("空串是true")
else:
    print("空串是false")

if s:
    print("true")
else:
    pass