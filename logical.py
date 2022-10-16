#Mantıksal Operatörler

x = 6
result = 5 < x < 10 #True

#AND operatörü
result = (x > 5) and (x < 10) #True
#True, True => True
#True, False => False
#False, False => False

#OR operatörü 
result = (x > 5) or (x % 2 == 0) #True
#True, True => True
#True, False => True
#False, False => False

#NOT operatörü
result = not(x > 5) #False
#True => False
#False => True

# x, 5-10 arasında olan bir çift sayı mı?
result = ((x > 5) and (x < 10)) and (x % 2 == 0) #True

print(result) 