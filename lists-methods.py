import numbers


numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

value = min(numbers) #1
value = max(numbers) #16

value = min(letters) #a
value = max(letters) #y

value = numbers[3:6] #[16, 4, 9]
value = numbers[:3]  #[1, 10, 5]
value = numbers[4:]  #[4, 9, 10]

numbers[4] = 40 # 4. indexteki elemanın değeri 40 olur.
numbers.append(49) #Listeye 49 elemanı eklenir.
numbers.insert(3, 78) # 3. indexe 78 elemanını ekler.
numbers.insert(-1, 100) #Listenin en sonuna 100 elemanını ekler.
numbers.pop() #Listenin son elemanını siler.
numbers.pop(0) #Listenin 0. indexini siler.
numbers.remove(49) #Listeden 49 elemanını sil.
numbers.sort() #Listeyi sıralar.
numbers.reverse() #Listeyi tersten sıralar. (Büyükten küçüğe)
numbers.clear() #Listenin tüm elemanlarını siler.
letters.sort() #Listeyi alfabetik sıralar.
letters.reverse() #Listeyi tersten alfabetik olarak sıralar.
print(letters)

print(len(numbers)) #Numbers dizisinin uzunluğunu verir.
print(len(letters)) #Letters dizisinin uzunluğunu verir.
print(numbers.count(10)) #Numbers dizisinde kaç tane 10 olduğunun sayısını döndürür.
print(letters.count('a')) #Letters dizisinde kaç tane a olduğunun sayısını döndürür.
print(value)
