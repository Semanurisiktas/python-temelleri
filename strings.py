name = 'Semanur'
surName = 'Işıktaş'
age = 20

print('My name is ' + name + ' ' + surName + ' and I am ' + str(age) + ' years old.')
# My name is Semanur Işıktaş and I am 20 years old.
print('My name is ' + name + ' ' + surName + ' and \nI am ' + str(age) + ' years old.')
# My name is Semanur Işıktaş and 
# I am 20 years old.

greeting = 'My name is ' + name + ' ' + surName + ' and \nI am ' + str(age) + ' years old.'
print(greeting)
print(greeting[0])      #M 
print(greeting[4])      #a
length = len(greeting)
print(len(greeting))    # 50 karakterli
print(greeting[length-1]) #Index numarası 0'dan başladığı için -1 yaparız. Son karakterin indexini buluruz
print(greeting[-1])     #Son karakteri bulur.

print(greeting[2:5])    #2. indexten 5. indexe kadar yazdırır.
print(greeting[3:])     #3. indexten son karaktere kadar yazdırır.
print(greeting[:15])    #Baştan başlayıp 15. indexe kadar yazdırır.
print(greeting[2:40:2]) #2.indexten 40. indexe 2şer 2şer gider.

