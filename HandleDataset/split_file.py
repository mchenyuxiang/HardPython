#-*-coding:utf-8-*-

file_input_object = open('./ml-1m/ratings_handle.dat')
file_output_base_object = open('./ml-1m/data/u1.base','w+')
file_output_test_object = open('./ml-1m/data/u1.test','w+')

count = 0

for one in file_input_object:
    count = count + 1
    if count % 5 == 0:
        file_output_test_object.write(one)
        count = 0
    else:
        file_output_base_object.write(one)