# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# # и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# # Для дочерних объектов указывайте родительскую директорию.
# # Для каждого объекта укажите файл это или директория.
# # Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
# # с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


end_data = []
x_path = "c:\\dir_for_test"


def func_20():
    sum = 0
    for i in os.walk(x_path, topdown = False):
        list_files = i[2]
        dir_name = i[0].rsplit('\\')[ - 1]
        way = i[0]
        if len(way) > 0 :
            for file in list_files:
                size_f = os.path.getsize(way + '\\' + file)
                end_data.append({'type': 'file',
                                'name': file,
                                'adr': way,
                                'size': size_f})
                sum += size_f
            end_data.append({'type': 'dir',
                                'name': dir_name,
                                'adr': way,
                                'size': sum})
        print(end_data)
    return end_data


def write_file(data, nameF):
    with open(nameF + ".json", "w") as file_1:
        json.dump(data, file_1)
    with open(nameF + ".csv", 'w', newline = '', encoding = 'utf - 8') as file_2:
        csv_write = csv.DictWriter(file_2, fieldnames = [ * data[0]])
        csv_write.writeheader()
        csv_write.writerows(data)
    with open(nameF + ".pickle", 'wb') as file_3:
        pickle.dump(data, file_3)


func_20()
write_file(end_data, 'example')
