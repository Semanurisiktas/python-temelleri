from unicodedata import name

names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1. 'Cenk' ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)

# 2. 'Sena' değerini listenin başına ekleyiniz. 
names.insert(0, 'Sena')
print(names)

# 3. 'Deniz' ismini listeden çıkarın.
names.remove('Deniz')
print(names)

# 4. 'Deniz' isminin indexi kaçtır?
index = names.index('Deniz')
print(index)

# 5. 'Ali' listenin elemanı mıdır?
print('Ali' in names)

# 6. Liste elemanlarını ters çeviriniz.
names.reverse()
years.reverse()
print(names)
print(years)

# 7. Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 8. Years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years) 

# 9. str = 'Chevrolet,Dacia' karakter dizisini listeye çeviriniz.
str = 'Chevrolet, Dacia'.split(',')
print(str)

# 10. years dizisinin en büyük ve en küçük elemanı nedir?
years.sort()
enBuyuk = years[-1]
enKucuk = years[0]
print(f'En büyük: {enBuyuk}')
print(f'En küçük: {enKucuk}')

# 11. years dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))

# 12. years dizisinin tüm elemanlarını siliniz. 
years.clear()
print(years)

# 13. Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
marka1 = input('1. markayı giriniz: ')
marka2 = input('2. markayı giriniz: ')
marka3 = input('3. markayı giriniz: ')

marka = [marka1, marka2, marka3]
print(marka)

# IKINCI YOL
markalar = []

marka = input('1. markayı giriniz: ')
markalar.append(marka)

marka = input('2. markayı giriniz: ')
markalar.append(marka)

marka = input('3. markayı giriniz: ')
markalar.append(marka)

print(markalar)
