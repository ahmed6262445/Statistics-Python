from collections import defaultdict
my_list = [112, 86, 84, 99, 108, 102, 101, 95, 102, 87, 106, 123, 105, 107, 91, 124, 103, 108, 94, 110, 142, 87, 89, 99, 129, 94, 115, 88, 117, 100, 95, 95, 107, 103, 76, 97, 79, 117, 108, 107, 69, 105, 91, 88, 106, 111, 92, 108, 108, 86, 118, 94, 109, 92, 111, 106, 100, 86, 100, 100, 97]
my_dict = defaultdict(list)

for  i in range( len(my_list) ):
    key = int(my_list[i]/10)
    value = my_list[i]%10

    my_dict[key].append(value)    
    my_dict[key].sort()

sorted(my_dict.keys()) 

for key,value in sorted(my_dict.items()):
    print(f"{key}:\t{value} \ttotal :{len(value)}") 