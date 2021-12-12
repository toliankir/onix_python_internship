# main.py
from operator import itemgetter

input_data: list = [[1, 3, 3, 4], [2, 1, 3, 5],
                    [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]


def main():
    print(input_data)
    sorted_list: list = sort_list(input_data)
    print(sorted_list)
    mapped_dict: dict = map_to_dictonary(sorted_list)
    print(mapped_dict)
    sorted_dict: dict = sort_dictonary(mapped_dict)
    print(sorted_dict)
    generated_set: set = to_set(sorted_dict)
    print(generated_set)
    result_str: str = set_to_str(generated_set)
    print(result_str)


def sort_list(input_list: list):
    return sorted(input_list, key=itemgetter(1))


def map_to_dictonary(input_list: list):
    return dict((item[1], [item[0]] + item[2:4]) for item in input_list)


def sort_dictonary(input_dict: dict):
    output_dict: dict = input_dict.copy()
    for _, value in output_dict.items():
        value.sort(reverse=True)
    return output_dict

def to_set(input_dict: dict):
    output_set: set = set()
    for _, value in input_dict.items():
        output_set.update(value)
    return output_set

def set_to_str(input_set: set):
    return ", ".join(map(str, input_set))


main()