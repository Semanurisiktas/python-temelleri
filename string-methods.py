from dataclasses import replace


message = 'Hello There. My name is Semanur Işıktaş'

message = message.upper() #Tüm karakterleri büyük harfle yazar.

message = message.lower() #Tüm karakterleri küçük harfle yazar.

message = message.title() #Tüm karakterlerin baş harfini büyük harfle yazar.

message = message.capitalize()  #Sadece ilk harfi büyük harfle yazar.

message = message.strip() #Kullanıcının girdiği kelimenin başını ve sonunu kontrol eder. (Boşluk var mı vs.)

message = message.split() #Kullanıcının girdiği cümledeki her boşluktan sonra bir karakter olarak diziye atar. => ['Hello', 'there.', 'my', 'name', 'is', 'semanur', 'işiktaş']
# print(message[2]) dersek my kelimesini ekrana yazdırır.

message = message.split('.') #Kullanıcının girdiği cümleyi her noktadan sonra bir karakter olarak alır.
#['Hello There', 'My name is Semanur Işıktaş']

message = ' '.join(message) #Split ile ayrılan kelimeleri tekrar birleştirir.
message = '*'.join(message) #Split ile ayrılan kelimeleri tekrar birleştirir ve aralarına * koyar.
print(message)

index = message.find('Semanur') #Cümlede Semanur kelimesi var mı yok mu kontrol eder.
print(index) #EKRAN ÇIKTISI : 24 => 24. indexten itibaren Semanur kelimesi başlıyor. 
             #EKRAN ÇIKTISI : -1 olursa o kelime cümlede yoktur.

isFound = message.startswith('H') #Cümlede H harfi ile başlayan karakter var mı yok mu kontrol eder.
print(isFound) #Ekran çıktısı true ya da false döner.

isFound = message.endswith('n') #Cümlede n harfi ile biten karakter var mı yok mu kontrol eder.
print(isFound) #Ekran çıktısı true ya da false döner.

message = message.replace('Semanur', 'Çınar') #Cümle içindeki Semanur yazısını Çınar yapar.
print(message) #Hello There. My name is Çınar Işıktaş

message = message.replace(' ', '*') #Cümle içindeki boşlukları * yapar.
print(message) #Hello*There.*My*name*is*Çınar*Işıktaş

message = message.replace('ö','o').replace('ü','u').replace('ı','i').replace('ç','c').replace('ş','s')
print(message) #Türkçe karakterleri ingilizce alfabesine göre uyarlar.

message = message.center(100)
print(message) # 100 karakterlik bir alanda yazıyı ortalar.






