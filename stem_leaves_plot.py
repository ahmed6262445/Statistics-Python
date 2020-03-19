from collections import defaultdict
# my_list = [112, 86, 84, 99, 108, 102, 101, 95, 102, 87, 106, 123, 105, 107, 91, 124, 103, 108, 94, 110, 142, 87, 89, 99, 129, 94, 115, 88, 117, 100, 95, 95, 107, 103, 76, 97, 79, 117, 108, 107, 69, 105, 91, 88, 106, 111, 92, 108, 108, 86, 118, 94, 109, 92, 111, 106, 100, 86, 100, 100, 97]

def make_stem_leaves_plot(number_list):
    """
        Arguments:
        number_list (list)

        Return:
            Returns stem and leaves plot as dictionary of list
    """
    dict_list = defaultdict(list)

    for i in range(len(number_list)):
        key = int(int(number_list[i])/10)
        value = int(number_list[i])%10
        dict_list[key].append(value)    
        dict_list[key].sort()

    new_dict = defaultdict(list)

    for key,value in sorted(dict_list.items()):
        new_dict[key] = value
    return new_dict