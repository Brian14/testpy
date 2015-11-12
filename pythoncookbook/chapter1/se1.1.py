__author__ = 'bao'

testString = 'qwertyuiop'
thelist = list(testString)

for c in thelist:
    print c


results = [str.upper(c) for c in thelist]
print results