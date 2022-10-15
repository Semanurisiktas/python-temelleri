'''
ogrenciler = {
    '120' : {
        'ad' : 'Ahmet',
        'soyad' : 'Çelik',
        'telefon ' : '12365'
    },
    '125' : {
        'ad' : 'Ayşe',
        'soyad' : 'Yılmaz',
        'telefon ' : '12343'
    },
    '128' : {
        'ad' : 'Zeynep',
        'soyad' : 'Korkmaz',
        'telefon ' : '12348'
    }
}

1. Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
2. Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösteriniz.
'''
ogrenciler = {}
ogrenci_no = input('Öğrenci numarasını giriniz: ')
ogrenci_ad = input('Öğrenci adını giriniz: ')
ogrenci_soyad = input('Öğrenci soyadını giriniz: ')
ogrenci_tel = input('Öğrenci tel giriniz: ')

'''
ogrenciler[ogrenci_no] = {
    'ad' : ogrenci_ad,
    'soyad' : ogrenci_soyad,
    'telefon' : ogrenci_tel
}
print(ogrenciler) #{100: {'ad': 'Ali', 'soyad': 'Yılmaz', 'telefon': '12456'}}
'''

#İKİNCİ YOL : update ile birden fazla veriyi aynı anda liste üzerine ekleyebiliriz.
ogrenciler.update({
    ogrenci_no : {
        'ad' : ogrenci_ad,
        'soyad' : ogrenci_soyad,
        'telefon' : ogrenci_tel
    }
})
#ikinci öğrenci 
ogrenci_no = input('Öğrenci numarasını giriniz: ')
ogrenci_ad = input('Öğrenci adını giriniz: ')
ogrenci_soyad = input('Öğrenci soyadını giriniz: ')
ogrenci_tel = input('Öğrenci tel giriniz: ')
ogrenciler.update({
    ogrenci_no : {
        'ad' : ogrenci_ad,
        'soyad' : ogrenci_soyad,
        'telefon' : ogrenci_tel
    }
})

#üçüncü öğrenci
ogrenci_no = input('Öğrenci numarasını giriniz: ')
ogrenci_ad = input('Öğrenci adını giriniz: ')
ogrenci_soyad = input('Öğrenci soyadını giriniz: ')
ogrenci_tel = input('Öğrenci tel giriniz: ')
ogrenciler.update({
    ogrenci_no : {
        'ad' : ogrenci_ad,
        'soyad' : ogrenci_soyad,
        'telefon' : ogrenci_tel
    }
})

print(ogrenciler) #{100: {'ad': 'Ali', 'soyad': 'Turan', 'telefon': '1234'}, 200: {'ad': 'Semanur', 'soyad': 'Işıktaş', 'telefon': '157834'}, 300: {'ad': 'Eda', 'soyad': 'Çelik', 'telefon': '124578'}}

#********************
# 2. Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösteriniz.
print('*'*50)

ogrNo = input('Öğrenci numarasını giriniz: ')
ogrenci = ogrenciler[ogrNo] #Buradaki key ogrNo, value ise içindeki değerler oluyor. (Key-Value)
print(f"Aradğınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']}, soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}'dir.")

print('*'*50)
'''
**************************************************
Öğrenci numarasını giriniz: 100
Aradğınız 100 nolu öğrencinin adı: Ali, soyadı: Turan ve telefonu ise 1234'dir.
**************************************************
'''



