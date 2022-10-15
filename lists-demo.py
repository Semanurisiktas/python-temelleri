# 1. 'Bmw, Mercedes, Opel, Mazda' elemanlarına sahip bir liste oluşturunuz.
car_list = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
print(car_list)

# 2. Liste kaç elemanlıdır?
print(len(car_list)) #4

# 3. Listenin ilk ve son elemanı nedir?
listFirst = car_list[0] #Bmw
listEnd = car_list[len(car_list)-1] #Mazda
#KISA YOL
#listEnd = car_list[3]
print(listFirst, listEnd)

# 4. Mazda değerini Toyota ile değiştirin.
car_list[3] = 'Toyota'
print(car_list)

# 5. Mercedes listenin bir elemanı mıdır?
result = 'Mercedes' in car_list 
print(result) #True

# 6. Listenin -2 indexindeki değer nedir?
print(car_list[-2]) #Opel => -2 : Sondan ikinci eleman

# 7. Listenin ilk 3 elemanını alın.
print(car_list[:3])
#print(car_list[0:3])

# 8. Listenin son 2 elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin.
car_list[-2:] = ['Toyota', 'Renault']
print(car_list)

# 9. Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin.
newList = ['Audi', 'Nissan']
car_list += newList
print(car_list)
# newList = car_list + ['Audi', 'Nissan']
# print(newList)

# 10. Listenin son elemanını silin.
del car_list[-1]
print(car_list)

# 11. Liste elemanlarını tersten yazdırınız.
print(car_list[::-1]) # Listeyi ters yazdırır.
# print(car_list[::1]) => Listeyi düz yazdırır.

# 12. Aşağıdaki verileri bir liste içinde saklayınız.
    #studentA = Yiğit Bilgi 2010, (70,60,90)
    #studentB = Sena Turan 1999, (80,80,70)
    #studentC = Ahmet Turan 1998, (80,70,90)
studentA = ['Yiğit', 'Bilgi', 2010, (70,60,90)]
studentB = ['Sena', 'Turan', 1999, (80,80,70)]
studentC = ['Ahmet', 'Turan', 1998, (80,70,90)]

# 13. Liste elemanlarını ekrana yazdırınız.
students = [studentA, studentB, studentC]
print(students)

# result = 'Yiğit Bilgi 12 yaşında ve not ortalaması 73'
yas = 2022 - studentA[2]
ort = (studentA[3][0] + studentA[3][1] + studentA[3][2])/ len(studentA[3])
result = f'{studentA[0]} {studentA[1]} {yas} yaşında ve not ortalaması {ort:2.3}'
print(result)
