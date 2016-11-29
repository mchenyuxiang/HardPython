#-*-coding:utf-8-*-
import string

file_input_object = open('./ml-1m/ratings.dat')
file_output_object = open('./ml-1m/ratings_handle.dat','w+')


for one_text in file_input_object:
    file_output_str = one_text.split("::")
    one_text_str = " ".join(file_output_str)
    file_output_object.write(one_text_str)
