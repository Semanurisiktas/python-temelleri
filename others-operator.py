#Diğer operatörler

#Identity Operator: is => Referans bilgisini(aynı dersi tutup tutmadığını) kontrol eder.
x = y = [1, 2, 3]
z = [1, 2, 3]

print(x == y) #True
print(x == z) #True
print(x is y) #True
print(x is z) #False
print(x is not z) #True
# x ve y aynı referansa sahip iken z farklı referansa sahip.

#Membership Operator: in 
x = ['apple', 'banana']
print('banana' in x) #True

name = 'Semanur'
print('a' in name) #True
print('a' not in name) #False

