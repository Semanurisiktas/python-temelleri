#Value Types => number,string
x, y = 5, 25
x = y
y = 10 
#y'nin 10'a eşitlenmesi x'in değerini etkilemiyor çünkü atama sırasında değer ataması yapılıyor dolayısıyla x ve y farklı adreslerde tutulan verilerdir.
print(x,y) # 25, 10


#Reference Types => list,class
#Referans tipinde tanımlanan veri tipleri (örneğin; list) atanan değeri tutmak yerine değerin tutulduğu adresleri saklarlar. Adreslerin karşılığı olan veriler ise (["apple","banana"]) belleğin farklı bölgesinde tutulur.

a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"
print(a, b) # ["grape","banana"] , ["grape","banana"]
#a ve b listeleri içindeki veriler farklı adres bilgilerini tutan veri tipleridir. a = b dediğimizde b'nin adresi a'ya atanır ve sonuçta a ve b, aynı adresleri tutarlar. Dolayısıyla a ya da b'de yapılan bir değişiklik aynı adreste yapıldığından dolayı a ve b 'nin içeriği de aynı olmuş olur.