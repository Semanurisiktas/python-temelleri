# Karşılaştırma Operatörü

from unittest import result

a, b, c, d = 5, 5, 10, 4
result = (a == b) #True
result = (a == c) #False

userName = 'Semanur'
password = '12345'
result = ('smnr' == userName) #False
result = ('12345' == password) #True

result (a != b) #False
result (a != c) #True
result (a < c) #True
result (a > c) #False
result (a >= b) #True
result(True + False + 40) # 1+0+40 = 41

print(result) 
