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
print(arr[1,1,0])

