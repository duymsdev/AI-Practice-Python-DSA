import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],
                [[7,8,9],[10,11,12]]
                ])
print(arr)
print(arr.ndim)
#tại sao đây là mảng 3 chiều ? 
# nhìn vào mảng arr , ta thấy hai khối lớn từ 1 tới 6 và từ 7 tới 12 , là chiều 1
# nhìn vào mỗi khối , ta thấy có hai khối nhỏ hơn , là chiều 2
# nhìn vào khối con trong khối to , ta thấy có 3 phần từ , là chiều 3
print(arr[0,1,2]) # 1  , 2 , 3 : khối 1 ( 1 -> 6 ) , hàng 2 , phần tử thứ 3
print(arr[1,1,0]) # in ra 10 , khoi thu 2 , hang hai , cot mot
arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim : ', arr2[1,-1] , '\n\n') # in ra 10 ? 

# numpy array slicing
arr3 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr3[1:6]) # lay phan tu tu arr3[1] -> arr3[5] : 2,3,4,5,6 
# arr3[start : stop : step] 
print(arr3[4:]) # lay tu phan tu arr3[4] den het array
print(arr3[:4]) # lay phan tu tu dau den phan tu arr3[3]
print(arr3[-3:-1]) # voi a[-3] = 8 , a[-2] = 9 , a[-1] = 10 , lay den phan tu -2
print(arr3[1:8:2]) # [ start : end : step ]
print(arr3[::2])
arr4 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])
print(arr4[1,1:4]) # in ra 7 8 9  [ pham vi hamg ,vi tri cot] , duyet hang 2 , chon phan tu thu 2 toi het 3 
print(arr4[0:2,2]) # in ra 3 8 [ pham_vi_hang , vi_tri_cot] , duyet hang 1 , hang 2 , chon cot so 2 roi chon xuong
print(arr4[0:2 , 1:4] , '\n\n') # in ra 2,3,4 . 7,8,9














#numpy data types
arr4 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])
print(arr4.dtype) # in ra int64 , tuc la các số nguyên được lưu dưới dạng 64 bit
arr5 = np.array(['apple','banana','cherry'])
print(arr5.dtype) # in ra <U6 , với U là unicode , 6 là độ dài tối đa của chuỗi trong mảng 
arr6 = np.array([1,2,3,4,5,6], dtype='S') # yeu cau numpy luu du liệu dưới dạng byte string ,
print(arr6)
print(arr6.dtype) # in ra |S1

arr7 = np.array([1,2,3,4], dtype='i4')
print(arr7)
print(arr7.dtype)

arr8 = np.array([1.1,2.1,3.1])
newarr8 = arr8.astype('i')
print(newarr8,'hi')
print(newarr8.dtype)

arr9 = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)










# Numpy Array Copy vs View
print('\n \n \n')
arr10 = np.array([1,2,3,4,5,6])
a = arr10.copy()
arr10[0] = 123123
print(arr10)
print(a)

#use view
arr10 = np.array([1,2,3,4,5,6])
x = arr10.view()
arr10[0] = 42
print('\n' ,arr10)
print(x)

arr11 = np.array([1,2,3,4,5,6])
x = arr11.copy()
y = arr11.view()
print('\n Hiii\n', x.base)
print(y.base)









#Numpy Array Shape
# cách nhớ : shape có bao nhiêu số thì mảng có bấy nhiêu chiều .
# (2,4) -> 2 chiều 
# (1,2,3,4,5) -> 5 chiều 
print('\n\n\n')
arr12 = np.array([[1,2,3,4], [5,6,7,8]]) # tạo ra mảng , giống 1 bảng gồm 2 hàng 4 cột
# dưới đây cho biết kích thước của mảng , trả về một bộ số tuple
print(arr12.shape) #in ra (2,4) , đọc là 2 hàng 4 cột 
# ban đầu [1,2,3,4] chỉ là mảng 1 chiều , ndmin = 5 nghĩa là ép mảng phải có ít nhất 5 chiều .
arr13 = np.array([1,2,3,4], ndmin = 5)
print(arr13)
# đọc từ trái sang phải , 4 chiều đầu mỗi chiều chỉ có 1 phần tử ( là các lớp ngoặc bọc thêm ) , chiều cuối cùng có 4 phần tử .
print('Shape of array : ', arr13.shape)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.shape) # in ra so hang va so cot
print(a.ndim) # in ra so chieu ( cung bang so luong so trong shape )
print(a.size) # in ra tong so phan tu