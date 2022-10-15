'''
1. Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
Müşteri adı
Müşteri soyadı
Müşteri ad + soyad
Müşteri cinsiyet
Müşteri TC kimlik
Müşteri doğum yılı
Müşteri adres bilgisi
Müşteri yaşı
'''
musteriAd = 'Semanur'
musteriSoyad = 'Işıktaş'
musteriAdSoyad = musteriAd + ' ' + musteriSoyad
musteriCinsiyet = False #False:Kadın True:Erkek
musteriTC = '12345678901'
musteriDogumYili = 2002
musteriAdres = 'Havaalanı Mah. Gönlüm Sok. Sevgi Apartmanı Kat:10 Daire:61'
musteriYas = 2020 - musteriDogumYili

'''
2. Aşağıdaki siparişlerin toplam bilgisini hesaplayalım.
Sipariş 1 => 110 TL
Sipariş 2 => 1100.5 TL
Sipariş 3 => 356.95 TL
'''
siparis1 = 110
siparis2 = 1100.5
siparis3 = 356.95
siparisToplam = siparis1 + siparis2 + siparis3
print(siparisToplam)
