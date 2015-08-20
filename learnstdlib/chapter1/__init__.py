__author__ = 'bao'

import string

#captail word
s1 = 'The quick brown fox jumped over the lazy dog.'
t1 = string.capwords(s1)
print t1

# replace char
s2 = 'The quick brown fox jumped over the lazy dog.'
t2 = string.maketrans('abegiloprstz','463611092572')
r2 = s2.translate(t2)
print r2