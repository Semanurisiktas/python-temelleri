from unicodedata import name

#Pythonda tuple listeleri, list' e benzer ancak farkı tuple içindeki elemanlar değiştirilemez yani tuple listesine ekleme, silme ve güncelleme yapamayız.

#Tuple liste elemanları, parantez ile oluşturulur. Ayrıca parantez kullanmadan da tuple listesi oluşturmuş oluruz ancak okunabilirlik açısından parantez kullanabiliriz.

list = [1, 2, 3]
tuple = (1, 'iki', 3)
print(type(list)) # <class 'list'> 
print(type(tuple)) # <class 'tuple'>

print(list[2]) #3
print(tuple[2]) #3

print(len(list)) #3
print(len(tuple)) #3

list = ['Ali', 'Ayşe'] #['Ali', 'Ayşe']
tuple = ('Semanur', 'Zehranur', 'Semanur') #('Semanur', 'Zehranur', 'Semanur)


list[0] = 'Ahmet' #['Ahmet', 'Ayşe']
#tuple[0] = 'Damla' #HATA VERİR. tuple listlere tek bir elemana ekleme değiştirme yapılamaz.
print(list)
print(tuple)

print(tuple.count('Semanur')) #2
print(tuple.index('Zehranur')) #1 : 'Zehranur' elemanı ilk kaçıncı indexte varsa onun değerini döndürür.

list = ['Ali', 'Ayşe']
tuple = ('Semanur' , 'Zehranur')
names = ('Vedat', 'Fatih', 'Ercan') + tuple #('Vedat', 'Fatih', 'Ercan', 'Semanur', 'Zehranur')
print(names)