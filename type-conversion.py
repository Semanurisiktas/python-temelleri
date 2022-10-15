#input : Kullanıcıdan veri almamızı sağlar.
from pickle import TRUE

x = input('1. Sayı : ')
y = input('2. Sayı: ')
'''
toplam = (x + y)
print(toplam) #Ekrana XY yazar. (X:10 Y:20 ise Sonuç:1020)
'''

toplam = int(x) + int(y)
print(toplam) #Ekrana X+Y yazar. (X:10 Y:20 ise Sonuç:30)

#*******************************

x = 5               #int
y = 2.5             #float
name = 'Semanur'    #str
isOnline = True     #bool

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

#******************************

#TYPE CONVERSION
# int to float
x = float(x) # 5 => int iken 5.0 => float oldu.
print(x)
print(type(x))

# float to int
y = int(y) # 2.5 => float iken 2 => int oldu.
print(y)
print(type(y))

result = x + y # 5 + 2.5 = 7.5
print(result) # 7.5
print(type(result)) #float

result = str(x) + str(y) #string olarak toplayalım
print(result) # 52.5
print(type(result)) #str

# bool to str
isOnline = str(isOnline)
print(isOnline) #True
print(type(isOnline)) #str

# bool to int
isOnline = int(isOnline) # True = 1
print(isOnline) #1
print(type(isOnline)) #int