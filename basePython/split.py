#-*-conding:utf-8-*-
import string
file_input_object = open('u.item')
file_output_object = open('sep.item','w+')

for one_text in  file_input_object:
	one_text_split = one_text.split('|')[5:24]
	one_text_split_str = ",".join(one_text_split)
	file_output_object.write(one_text_split_str)

#one = file_input_object.readline()
#one_split = one.split('|')
#print one_split[6:24]
