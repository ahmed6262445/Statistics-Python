from collections import defaultdict

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