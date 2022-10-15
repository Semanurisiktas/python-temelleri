import re


name = 'Semanur'
surName = 'Işıktaş'
age = 20

print('My name is {} {}' .format(name,surName)) # {} yerine yazılması gereken format() kısmına yazılır.
print('My name is {0} {1}' .format(name,surName))
print('My name is {1} {0}' .format(surName,name))
print('My name is {n} {s}' .format(n=name, s=surName))

print('My name is {} {} and I am {} years old' .format(name,surName,age))

result = 200 / 700 # 0.2857142857142857
print('The result is {r:1.3}' .format(r=result))  # r:1.3 float degerin sonunda 3 karakter olur => 0.286
#The result is 0.286

print(f'My name is {name} {surName} and I am {age} years old')
