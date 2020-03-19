from stem_leaves_plot import make_stem_leaves_plot
import csv

my_list = []
# my_list = [112, 86, 84, 99, 108, 102, 101, 95, 102, 87, 106, 123, 105, 107, 91, 124, 103, 108, 94, 110, 142, 87, 89, 99, 129, 94, 115, 88, 117, 100, 95, 95, 107, 103, 76, 97, 79, 117, 108, 107, 69, 105, 91, 88, 106, 111, 92, 108, 108, 86, 118, 94, 109, 92, 111, 106, 100, 86, 100, 100, 97]

with open ('test.csv') as fi:
    reader = csv.reader(fi, delimiter=',')
    for line in reader:
        my_list.append(int(line[0]))

my_dict = make_stem_leaves_plot(my_list)
print(my_dict)