#Atama Operatörü

# x = 5
# y = 10
# z = 20

x, y, z = (5, 10, 20)
print(x, y, z) #5 10 20

x, y = y, x # y = y => x=y y=x
print(x, y, z) #10 5 20

x = x + 5 # x += 5 => Toplama
x = x - 5 # x -= 5 => Çıkarma
x = x * 5 # x *= 5 => Çarpma
x = x / 5 # x /= 5 => Bölme
x = x % 5 # x %= 5 => Mod alma
x = x // 5 # x //= 5 => Tam bölme
x = x ** 5 # x **= 5 => Üst alma

values = 1, 2, 3
print(values) #(1, 2, 3)
print(type(values)) # <class 'tuple'>

x, y, z = values
print(x, y, z) #1, 2, 3

values = 1, 2, 3, 4, 5
x, y, *z = values #x'e 1'i, y'e 2'yi geriye kalan elemanları ise z'ye dizi olarak atar.
print(x, y, z) #1 2 [3, 4, 5]
print(x, y, z[1]) #1 2 4










