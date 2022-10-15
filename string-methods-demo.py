website = 'http://www.sadikturan.com'
course = 'Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)'

# 1. ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
message = ' Hello World '
message = message.strip()
message = message.lstrip() # Left strip  (sol tarafı kontrol eder)
message = message.rstrip() # Right strip (sağ tarafı kontrol eder)
print(message)

# 2. 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result = 'www.sadikturan.com'
result = result.lstrip('www.')
result = result.rstrip('.com')
print(result)
# FARKLI BİR YOL :
# result = result.strip('w.moc) => w . m o c karakterlerini siler

# 3. 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
course = course.lower()
print(course)

# 4. 'website' içinde kaç tane a karakteri vardır? (count('a'))
message = 'website'
message = message.count('a')
print(message)

# 5. 'website', 'www' ile başlayıp 'com' ile bitiyor mu?
isFoundStart = website.startswith('www') #False
isFoundEnd = website.endswith('com') #True
print(isFoundStart, isFoundEnd)

# 6. 'website' içinde '.com' ifadesi var mı?
result = website.find('.com')
print(result) #Evet var, 21. indexte 
#index = website.find('.com', 0,10) => .com ifadesi 0-10 arasındaki karakterlerde var mı?
#result = course.rfind('python') => Arama yapmaya sağdan başlar.

# 7. 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha()
print(result) #False => Course karakterinde sayısal değerler de var.
#result = 'Hello'.isalpha() => True

result = course.isdigit()
print(result) #False => Course karakterinde string değerler de var.
#result = '123'.isdigit() => True

# 8. 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
message = 'Contents'
message = message.center(50,'*')
print(message)

#message = message.lcenter(50,'*') => Content yazısını sola yaslar ve sağına yıldız ekler.
#message = message.rcenter(50,'*') => Content yazısını sağa yaslar ve soluna yıldız ekler.

# 9. 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
course = course.replace(' ', '-')
print(course)

# 10. 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.
message = 'Hello World'
message = message.replace('World', 'There')
print(message) 

# 11. 'course' karakter dizisini boşluk karakterlerinden ayırın. 
course = course.split(' ')
print(course)