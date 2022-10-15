#Dictionary liste elemanlarına KEY ve VALUE değerlerine göre ulaşıp elemanlar üzerinde güncelleme yapabiliriz.

# dictionary = { 'Key' : 'Value' }
# 41 => 'Kocaeli'  34 => 'İstanbul'

import email

sehirler = ['Kocaeli', 'İstanbul']
plakalar = [41, 34]
print(plakalar[sehirler.index('İstanbul')]) #34

#print(plakalar['Kocaeli']) => 41
#print(plakalar['İstanbul']) => 34

plakalar = {'Kocaeli' : 41, 'İstanbul' : 34}
print(plakalar['Kocaeli']) #41
print(plakalar['İstanbul']) #34

plakalar['Ankara'] = 6
plakalar['Kocaeli'] = 'New Value'
print(plakalar) #{'Kocaeli': 'New Value, 'İstanbul': 34, 'Ankara': 6}

#*******************************************

users = {
    'sadikturan' : {
        'age' : 26,
        'roles' : ['admin', 'user'],
        'email' : 'sadikturan@gmail.com',
        'address' : 'kocaeli',
        'phone' : 1234453
    },
    'egecinar' : {
        'age' : 2,
        'roles' : ['user'],
        'email' : 'egecinar@gmail.com',
        'address' : 'istanbul',
        'phone' : 3456334
    }
}

print(users['egecinar']) 
#{'age': 2, 'roles' : ['user'], 'email': 'egecinar@gmail.com', 'address': 'istanbul', 'phone': 3456334}

print(users['sadikturan']['email']) #sadikturan@gmail.com
print(users['sadikturan']['roles'][0]) #admin








