# 1. Girilen 2 sayıdan hangisi büyüktür?
from cgi import print_arguments

sayi1 = int(input('1. sayıyı giriniz: '))
sayi2 = int(input('2. sayıyı giriniz: '))
result = (sayi1 > sayi2)
print(f"Birinci sayı: {sayi1} İkinci sayı: {sayi2}'dan büyük mü? : {result}")

# 2. Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti, değil ise kaldı yazdırın.
vize1 = int(input('1. vize notunu giriniz: '))
vize2 = int(input('1. vize notunu giriniz: '))
final = int(input('Final notunu giriniz: '))
ort = (((vize1+vize2) / 2) * 0.6  + final * 0.4)
print(f"Not ortalamanız: {ort} ve dersten geçme durumunuz {ort>=50}")

# 3. Girilen bir sayının tek mi çift mi olduğunu yazdırın.
sayi = int(input('Bir sayı giriniz: '))
print(f"Girdiğiniz sayı çift olma durumu {sayi%2==0}, tek olma durumu {sayi%2==1}")

# 4. Girilen bir sayının negatip pozitif olma durumunu yazdırın.
sayi = int(input('Bir sayı giriniz: '))
print(f"Girdiğiniz sayı negatif olma durumu {sayi<0}, pozitif olma durumu {sayi>0}")

# 5. Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
email = 'Semanurisiktass@gmail.com'
parola = 'abc123'

girilenEmail = input('Email: ')
girilenPassword = input('Parola: ')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (parola==girilenPassword.lower())
print(f"Girdiğiniz mailin doğru olma durumu {isEmail}, parolanın doğru olma ihtimali {isPassword}")
#lower() : Kullanıcının girdiği tüm karakterler küçük harf olur.
#strip() : Kullanıcının girdiği karakterin başındaki ve sonundaki boşlukları kaldırır.

