#Pythonda set listeleri, list' e benzer ancak fark olarak set içindeki elemanlar sıralanamaz (sort) ve indekslenemez yani set elemanlarına 0,1 şeklinde indeks numaraları ile ulaşamayız. Dolayısıyla set 'e eklediğimiz bir elemanın set listesi içinde hangi sırada olacağını bilemeyiz. Ayrıca set içerisindeki elemanlar tekrarlayamaz, her bir elemandan sadece bir tane olmalıdır, tekrarlayanlar silinir.

#Pythonda set oluşturmak için süslü parantezler kullanırız. 

fruits = {'apple', 'banana', 'orange'}
print(fruits) #{'banana', 'apple', 'orange'}
#print(fruits[0]) #HATA VERİR. set listeleri indexlenemez.

#Peki set listesinin elemanlarına nasıl ulaşırız?
for x in fruits:
    print(x)
    
fruits.add('cherry') #Tek eleman ekleme
print(fruits) #{'apple', 'cherry', 'banana', 'orange'}

fruits.update(['mango', 'grape']) #Liste olarak birden fazla eleman ekleme
print(fruits) #{'mango', 'apple', 'grape', 'banana', 'cherry', 'orange'}

fruits.add('apple') #Elemanlar tekrarlamaz. (2 kere apple yazmaz)
print(fruits) #{'orange', 'grape', 'cherry', 'mango', 'apple', 'banana'}

myList = [1,2,1,6,2,1,2,2,5] 
print(set(myList)) #{1, 2, 5, 6} => Tekrarlanan veriler listeye alınmaz.

fruits.remove('mango') #Mango elemanı listeden silinir.
print(fruits) #{'cherry', 'apple', 'orange', 'grape', 'banana'}

#fruits.discard('mango') => remove ile aynı işlemi yapar.

#fruits.pop() => Pop metodu listedeki son elemanı siliyordu fakat set listesinde sıralanma olmadığı için herhangi bir eleman silinebilir.

fruits.clear() #Listeyi siler.
print(fruits)
