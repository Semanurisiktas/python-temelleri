message = 'Hello There. My name is Semanur Işıktaş'.split()
# print(message)
print(message[0]) #Hello

my_list = [1, 2, 3]
my_list = [1, 'Semanur', True, 2.8]
print(my_list)

list1 = ['one', 'two', 'three']
list2 = ['four', 'five', 'six']
numbers = list1 + list2
print(numbers) #['one', 'two', 'three', 'four', 'five', 'six']
print(len(numbers)) #6 
print(numbers[2]) #three

userA = ['Sadık', 36]
userB = ['Çınar', 2]
#users = userA + userB ==>> ['Sadık', 36, 'Çınar', 2] Kullanıcının her bilgisi ayrı bir dizi olarak alınır.
users = [userA , userB] #[['Sadık', 36], ['Çınar', 2]] Kullanıcının her bilgisi bir dizi olarak alınır.
print(users)
print(users[0])  #userA olur
print(users[1])  #userB olur.

userBname = users[1] 
print(userBname[0]) #Ekrana sadece 'Çınar' yazdırılır.
#KISA YOL
print(users[1][0]) #Ekrana sadece 'Çınar' yazdırılır.
print(users[1][1]) #Ekrana 2 yazdırılır.