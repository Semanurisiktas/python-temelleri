website = 'http://www.sadikturan.com'
course = 'Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)'

# 1. 'course' karakter dizisinde kaç karakter bulunmaktadır?
length = len(course)
print(length)

# 2. 'website' içinden www karakterlerini alın.
print(website[7:10])

# 3. 'website' içinden com karakterlerini alın.
print(website[22:])
#print(website[22:25])
#print(length-3 :length)

# 4. 'course' içinden ilk 15 ve son 15 karakterlerini alın.
print(course[0:15])
print(website[-15:])

# 5. 'course' ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])

#********************************

name, surName, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'
# 6. yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#   'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
print(f'Benim adım {name} {surName}, Yaşım {age} ve mesleğim {job}')
print('Benim adım ' + name + ' ' + surName + ' , Yaşım ' + str(age) + ' ve mesleğim ' + job)
print('Benim adım {} {} , Yaşım {} ve mesleğim {}' .format(name,surName,age,job))
print('Benim adım {0} {1} , Yaşım {2} ve mesleğim {3}' .format(name,surName,age,job))


# 7. 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
text = 'Hello world'
text = text[0:6] + 'W' + text[7:] 
print(text)
# KISA YOL : text.replace('w, W')

# 'abc' ifadesini yan yana 3 defa yazdırın
result = 'abc' * 3
print(result)