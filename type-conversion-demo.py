'''
    Daire Alanı : πr2
    Daire Çevresi : 2πr
    Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (r: 3.14)

'''
yariCap = input('Yarıçapı giriniz: ')
yariCap = float(yariCap)
pi = 3.14
daireAlani = pi * (yariCap**2)
daireCevresi = 2 * pi * yariCap
print('Dairenin Alanı : ', daireAlani)
print('Daire Çevresi: ', daireCevresi)
#Yan yana yazmak istersek =>> float değerindeyken str birleştirmesi yapamayız. float to str yapmalıyız
#print('Dairenin Alanı : ' + str(daireAlani) + ' ' + 'Dairenin Çevresi : ' + str(daireCevresi))