import email

# 1. Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = int(input('Bir sayı giriniz: '))
result = (0 < sayi < 100)
print(f"Girilen sayı 0-100 arasında mı? : {result}")

# 2. Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input('Bir sayı giriniz: '))
print(f"Girilen sayının çift olma durumu: {sayi%2==0}, tek olma durumu: {sayi%2==1}")

# 3. Email ve parola bilgileri ile giriş kontrolü yapınız.
Email = 'Semanurisiktass@gmail.com'
Password = 'abc123'

girilenEmail = input('Email giriniz: ')
girilenPassword = input('Parola giriniz: ')

result = (girilenEmail == Email) and (girilenPassword == Password)
print(f"Girilen bilgilerin doğru olma durumu: {result}")

# 4. Girilen 3 sayıyı büyüklük olarak sıralayınız.
sayi1 = int(input('1. sayıyı giriniz: '))
sayi2 = int(input('2. sayıyı giriniz: '))
sayi3 = int(input('3. sayıyı giriniz: '))

result = (sayi1 > sayi2) and (sayi1 > sayi3)
print(f"1. sayı en büyük sayıdır : {result}")

result = (sayi2 > sayi1) and (sayi2 > sayi3)
print(f"2. sayı en büyük sayıdır : {result}")

result = (sayi3 > sayi2) and (sayi3 > sayi1)
print(f"3. sayı en büyük sayıdır : {result}")

# 5. Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#   Eğer ortalama 50 ve üstündeyse geçti, değil ise kaldı yazdırın.
#   a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#   b-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1 = int(input('1. vize notunuzu giriniz: '))
vize2 = int(input('2. vize notunuzu giriniz: '))
final = int(input('Final notunuzu giriniz: '))

ort = ((vize1 + vize2) / 2) * 0.6 and (final * 0.4)
result = ((ort >= 50) and (final > 50) ) or (final >= 70)
print(f"Öğrencinin ortalaması: {ort}, geçme durumu: {result}")

# 6. Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#   Formül : ( Kilo/boy uzunluğunun karesi )
#   0 - 18.4    => Zayıf
#   18.5 - 24.9 => Normal
#   25.0 - 29.0 => Fazla Kilolu
#   30.0 - 34.9 => Şişman (Obez)

name = input('Adınızı giriniz: ')
kg = float(input('Kilonuzu giriniz: '))
hg = float(input('Boyunuzu giriniz: '))

index = (kg) / (hg ** 2)
zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.5) and (index <= 24.9)
kilolu = (index > 25.0) and (index <= 29.0)
obez = (index > 30.0) and (index <= 34.9) 

print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}")
