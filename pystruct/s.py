# -*- coding: utf-8 -*-
import struct

a = 20
b = 400

s = struct.pack("ii", a, b)

print 'length:', len(s)
print s
print repr(s)