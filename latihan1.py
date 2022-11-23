list1=['hello','program','Teknik','Informatika',1]
print('=====Akses List=====')
print(list1)
print(list1[2])
print(list1[1:4])
list1.pop()
print(list1)
print()
print('=====Ubah Element=====')
list1[3] = 'Manajemen'
print(list1)
list1[3:] = 'Sipil',2
print(list1)
print()
print('=====Tambah Element=====')
list2 = list1[:2]
print(list2)
list2.append('semester')
list2.append(3)
print(list1+list2)

