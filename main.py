from stem_leaves_plot import make_stem_leaves_plot
import csv

my_list = []

with open ('test.csv') as fi:
    reader = csv.reader(fi, delimiter=',')
    for line in reader:
        my_list.append(int(line[0]))

my_dict = make_stem_leaves_plot(my_list)
print(my_dict)