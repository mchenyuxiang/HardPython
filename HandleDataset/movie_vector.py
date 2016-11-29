#-*-coding:utf-8-*-
import string

file_input_object = open('ml-1m/movies.dat')
file_movie_object = open('ml-1m/item.dat')
file_output_object = open('ml-1m/data/sep1m.item','w+')

dict_movie = {}

for one_text in file_movie_object:
    dict_movie[one_text.split(" ")[1].strip('\n')]=one_text.split(" ")[0]

# for one in dict_movie.keys():
#     print one

count = 0
for one_data in file_input_object:
    count = count + 1
    temp = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
    print count

    if int(one_data.split("::")[0]) != count:
        gap = abs(int(one_data.split("::")[0])-count)
        for i in range(gap) :
            temp_d = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
            temp_d = ','.join(temp_d)
            file_output_object.write(temp_d + '\n')
            count = count + 1
    for temp_movie in one_data.split("::")[2].split("|"):
        t = dict_movie[temp_movie.strip('\n')]
        temp[int(t) - 1] = '1'
    temp = ','.join(temp)
    file_output_object.write(temp + '\n')


