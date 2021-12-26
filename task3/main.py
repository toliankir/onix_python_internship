import csv
import json

CSV_FILENAME = "data.csv"
JSON_FILENAME = "data.json"


def f1(x):
    return x / (x + 100)


def f2(x):
    return 1 / x


def f3(x, x_f1, x_f2):
    return (20 * (x_f1 + x_f2))/x


def x_generator():
    for x in range(5, 90):
        yield x


def func_result_generator():
    for x in x_generator():
        x1 = f1(x)
        x2 = f2(x)
        yield (x, x1, x2, f3(x, x1, x2))


def write_csv_file(file: str, data_dict: dict):
    with open(file, "w") as csv_file:
        fieldnames = ["x", "f1(x)", "f2(x)", "f3(x)"]
        csv_writer = csv.DictWriter(csv_file, fieldnames)
        csv_writer.writeheader()
        for (key, value) in data_dict.items():
            csv_writer.writerow({fieldnames[0]: key, fieldnames[1]: value[0],
                                 fieldnames[2]: value[1], fieldnames[3]: value[2]})


def read_csv_file(file: str):
    with open(file, "r") as csv_file:
        csv_reader_data = csv.reader(csv_file)
        next(csv_reader_data)
        return list(csv_reader_data)


def write_json_file(file: str, data_list: list):
    with open(file, "w") as json_file:
        json.dump(data_list, json_file, indent=2)


def main():
    data_dict: dict = dict((func_res[0], [func_res[1], func_res[2], func_res[3]])
                           for func_res in func_result_generator())
    write_csv_file(CSV_FILENAME, data_dict)
    data_list = read_csv_file(CSV_FILENAME)
    write_json_file(JSON_FILENAME, data_list)


main()
