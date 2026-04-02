import numpy as np
"Q1"
# import numpy as np
# print(np.__version__)

"Q2"

# arr = np.array([10, 20 , 30 ,40 ,50 ])
# print( type(arr))

"Q3"

# arr = np.arange(1,4)
# lis = [1,2,3]
# print(f'arr + arr = {arr + arr} ')
# print(f' list + lis = { lis + lis }')

"Q4"

# arr = np.arange(1,4)
# lis = [5,10,15]
# print(f'arr * arr = {arr * 3 } ')
# print(f' list * lis = { lis * 3 }')

"Q5"

# arr = np.array([ 100 , 200 , 300 , 400 , 500 , 600 ])
# print(f' dtype of arr is { arr.dtype }')
# print(f' shape of arr is { arr.shape}')
# print(f' size of arr is { arr.size }')
# print(f' ndim of arr is { arr.ndim}')
# print(f' nbytes of arr is { arr.nbytes }')

"Q6"

# arr = np.array([[ 1 , 2 , 3 ] , [ 4 , 5 , 6 ]])
# print(" Array : \n " , arr)
# print(arr.shape)
# print( arr.ndim )
# print( arr.size )

"Q7"

"i"
# arr = np.array([1 , 2 , 3 ] , dtype = np.int8 )
# print( arr.dtype  )
"ii"
# arr = np.array( [ 1.5 , 2.5 , 3.5 ] , dtype = np.float32)
# print( arr.dtype )
"iii"
# arr_bool = np.array ( [ True , True , False ] , dtype = np.bool )
# print( arr_bool.dtype )

"Q8"

# arr = np.array([ 1 , 2 , 3.14 ])
# arr_2 = np.array ( [ 1 , 2 , "hello"] )
# print( arr.dtype ,"\n", arr_2.dtype )

"Q9"

# import sys
# n = 10000
# # list side 
# py_lis = list( range (n) )
# list_size = sys.getsizeof( py_lis )
# print(f' List container size : {list_size : ,} bytes ')
# # array side 
# arr = np.arange ( n )
# arr_size = ( arr.nbytes )
# print(f' array container size : {arr_size : ,} bytes ')

"Q10"

# arr = np.array ( [ 78 , 85 , 92 , 56  , 74 , 88 , 95  , 67 , 81 , 73 ])
# print( arr.max ( ))
# print( arr.min ( ))
# print( arr.sum ( ))
# print( arr.std () )
# print( arr.mean ( ))

'''MID_SECTION_START''''NUMPY'''

"Q11"
# import time
# n = 1000000
# # list_test
# a_list = list (range( n ))
# b_list = list ( range ( n ))
# st_time = time.time()
# total_list = ( a_list [i] + b_list [i] for i in range ( n ) )
# end_time = time.time()
# print(f"Python List Time : {end_time - st_time:.4f} seconds")
# # np test
# arr_1 = np.arange( n )
# arr_2 = np.arange ( n )
# st_time = time.time()
# total_np = arr_1 + arr_2
# end_time = time.time()
# print(f"Python Numpy Time : {end_time - st_time:.4f} seconds")

"Q12"

# arr = np.array ([1.1, 2.7, 3.5, 4.9] , dtype = np.float64)
# # i
# arr_2 =  arr.astype (np.int32 )
# print(f'dtyp of {arr_2} is { arr_2.dtype} ' )
# # ii
# arr_2 =  np.round(arr).astype (np.int32 )
# print(f'dtyp of {arr_2} is { arr_2.dtype} ' )
# "diff is clear rounded by defult round is gives uppre number as compared to the without round"
# # iii
# arr_2 =  arr.astype (np.bool )
# print(f'dtyp of {arr_2} is { arr_2.dtype} ' )

"Q13"
