'''
Created on Feb 2, 2017

Trung Tam Tin Hoc - DH KHTN
'''
x = 15
y = 12
print('Binary of x =', bin(x), ', Binary of y =', bin(y))
print('x & y =', bin(x & y))
#   1111
# & 1100
# = 1100
print('x | y =', bin(x | y))
#   1111
# | 1100
# = 1111
print('x ^ y =', bin(x ^ y))
#   1111
# | 1100
# = 0011
print('~x =', bin(~x))
#  ~1111
# = -10000
print('x << 2 =', bin(x << 2))
#   1111
# << 2
# = 111100
print('y >> 2 =', bin(y >> 2))
#   1111
# >> 2
# = 11