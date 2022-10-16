x, y, z = 2, 5, 107
numbers = 1, 5, 7, 10, 6

# 1. Kullanıcıdan aldığınız 2 sayının çarpımı ile x, y, z toplamının farkı nedir ?
sayi1 = int(input('1. Sayıyı giriniz: '))
sayi2 = int(input('2. Sayıyı giriniz: '))
carpim = (sayi1*sayi2)
toplam = (x + y + z)
print(carpim-toplam)

# 2. y'nin x'e kalansız bölümünü hesaplayınız.
print(y//x)

# 3. (x,y,z) toplamının mod 3'ü kaçtır?
print(toplam%3)

# 4. y'nin x. kuvvetini hesaplayınız.
print(y**x)

# 5. x, *y, z = numbers işlemine göre z'nin küpü kaçtır?
x, *y, z = numbers #1 [5, 7, 10] 6
print(z**3) #6'nın küpü : 216

# 6. x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
print(y[0]+ y[1] + y[2]) #22
