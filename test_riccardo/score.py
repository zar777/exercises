import operator
import os


def save_data(file_name):
    map_data = {}
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            split_line = line.strip('\n').split(',')
            map_data[split_line[0]] = split_line[1]
    map_data.items()
    return map_data


def sort_by_names(data):
    sorted_names = sorted(data.items())
    return sorted_names


def sort_by_scores(data):
    sorted_value = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_value


def save_result(data, file_dest):
    with open(file_dest, "w") as result:
        for pair in data:
            result.write(pair[0] + "," + pair[1] + os.linesep)


def score(source_file, file_dst, flag):
    data = save_data(source_file)
    sorted_result = None
    if flag == "names":
        sorted_result = sort_by_names(data)
    elif flag == "scores":
        sorted_result = sort_by_scores(data)
    if sorted_result is not None:
        save_result(sorted_result, file_dst)

if __name__ == '__main__':
    source_file = "/home/gianluca/Documents/test_scores/score_data.txt"
    file_sort_names = "/home/gianluca/Documents/test_scores/sort_names"
    file_sort_scores = "/home/gianluca/Documents/test_scores/sort_scores.txt"
    print score(source_file, file_sort_names, "names")