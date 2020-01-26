# -*- coding: utf-8 -*-
# Version 1.1.0

import os
from time import sleep as delay
from re import sub
from statistics import median_high, median_low, median
from subprocess import Popen, PIPE

variab = input("Enter process name as 'tasklist' (ex. chrome.exe): ")
proc = Popen(["tasklist", '/FI', "IMAGENAME eq {0}".format(variab), "/FO", "TABLE", "/NH"], stdout=PIPE, shell=True)
# data - contain strings receive from windows utility "Tasklist"
data = proc.stdout.readlines()
clearNumber = 0
units_of_memory = ["KB", "K", "К", "КБ"]
statistic_storage = []
longest_string = {}
border_head = chr(9556) + "="*116 + chr(9559)
border_bottom = chr(9562) + "="*116 + chr(9565)

def detail_log(debug=0):
    with open(full_path + f'\\{variab[0:len(variab) - 4]}.txt', "w") as file:
        file.write(
            share_output_text + " " + f"or {round(uses_mb, count_num_after_dot)} MB or {round(uses_bytes, count_num_after_dot)} Bytes.\n")
        file.write(f"Total processes - {total_processes}.\n")
        file.write(f"Average value used RAM per process - {round(uses_mb / total_processes, count_num_after_dot)} MB\n")
        file.write(
            f"Median value used RAM per process - {median(statistic_storage) / 1024} MB, Low, "
            f"High median {median_low(statistic_storage) / 1024}, "
            f"{median_high(statistic_storage) / 1024} in MB")

    return debug


for i in range(1, len(data)):
    # ==================================================================
    # Пробегаем по всем элементам тасклиста и обрабатываем вывод.
    # После обработки суммируем и записываем в файл, который создается в дериктории запуска скрипта.
    # ==================================================================
    # In english
    # After receiving a list of a task begun processing him.
    # Then summarize and write all to file, which will be created in the directory is running this script.
    # ==================================================================
    trigger = 0
    while trigger == 0:

        for j in units_of_memory:
            if (j in sub(r"\s+", "||", data[i].decode("cp866").replace(r"\s", "")).split("||")[5] and
                    sub(r"\s+", "||", data[i].decode("cp866").replace(r"\s", "")).split("||")[5].isdigit() is not True):
                dirty_number = sub(r"\s+", "||", data[i].decode("cp866").replace(r"\s", "")).split("||")[4]
                clearNumber = int(sub(r",", "", dirty_number))

                statistic_storage.append(clearNumber)
                trigger = 1
                break

        if trigger != 1:
            print(f"Received value from \"Tasklist\" doesn't contain units - {units_of_memory}")
            break

if len(statistic_storage) != 0:
    total_used = sum(statistic_storage)
    uses_mb = total_used / 1024
    uses_gb = total_used / 1024 / 1024
    uses_bytes = total_used * 1024
    total_processes = len(data) - 1
    count_num_after_dot = 3

    share_output_text = f"The process uses {round(uses_gb, count_num_after_dot)} GB of memory (RAM)"
    full_path = os.path.dirname(os.path.abspath(__file__)) + "\\output"

    if os.path.exists(full_path):
        detail_log()
    else:
        os.mkdir(full_path)
        detail_log()

    print(border_head)

    a_1 = chr(9553) + " " +share_output_text
    a_2 =f"║ Detail info available by path \'{full_path}\' in file \'{variab[0:len(variab) - 4]}.txt\' "
    a_3 = f"║ Bye!"

    longest_string["a_1"] = len(a_1)
    longest_string["a_2"] = len(a_2)
    longest_string["a_3"] = len(a_3)
    length_head = len(border_head)
    for i in longest_string:
        if length_head > longest_string[i]:
            if i == "a_1":
                space = (length_head - longest_string[i]) - 1
                a_1 = a_1 + " "*space + "║"
            elif i == "a_2":
                space = (length_head - longest_string[i]) - 1
                a_2 = a_2 + " " * space + "║"
            elif i == "a_3":
                space = (length_head - longest_string[i]) - 1
                a_3 = a_3 + " " * space + "║"

    print(a_1 + "\n" + a_2 + "\n" + a_3)
    print(border_bottom)

elif len(statistic_storage) == 0:
    print("INFO: No tasks are running which match the specified criteria.")


delay(10)
