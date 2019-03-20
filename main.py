# -*- coding: utf-8 -*-
# Version 1.0.0

from subprocess import Popen, PIPE
from re import sub
from time import time

variab = input("Enter process name as 'tasklist': ")
proc = Popen(["tasklist", '/FI', "IMAGENAME eq {0}".format(variab), "/FO", "TABLE", "/NH"], stdout=PIPE, shell=True)
data = proc.stdout.readlines()
clearNum = 0

for i in range(1, len(data)):
    # ==================================================================
    # Пробегаем по всем элементам тасклиста и обрабатываем вывод.
    # После обработки суммируем и записываем в файл, который создается в дериктории запуска скрипта.
    # ==================================================================
    # In english
    # After receiving a list of a task begun processing him.
    # Then summarize and write all to file, which will be created in the directory is running this script.
    # ==================================================================

    if(("KB" in sub(r"\s+", "||", data[i].decode("cp866").replace(r"\s", "")).split("||")[5] or "КБ" in sub(r"\s+", "||", data[i].decode("cp866").replace(r"\s", "")).split("||")[5] or "K" in sub(r"\s+", "||", data[i].decode("cp866").replace(r"\s", "")).split("||")[5])
            and (sub(r"\s+", "||", data[i].decode("cp866").replace(r"\s", "")).split("||")[5].isdigit() != True)):

        Num = sub(r"\s+", "||", data[i].decode("cp866").replace(r"\s", "")).split("||")[4]
        clearNum += int(sub(r",", "", Num))
    else:
        Num = sub(r"\s+", "||", data[i].decode("cp866").replace(r"\s", "")).split("||")[4] + \
              sub(r"\s+", "||", data[i].decode("cp866").replace(r"\s", "")).split("||")[5]
        clearNum += int(sub(r",", "", Num))

with open(f'{variab[0:len(variab) - 4]}.txt', "w") as file:
    file.write("Memory is busy process: {0} bytes, {1} megabytes, {2} kilobytes \nTotal process: {3}".format(
        clearNum * 1024, clearNum / 1024, clearNum, len(data) - 1))

print("Memory is busy process: {0} bytes, {1} megabytes, {2} kilobytes".format(clearNum * 1024, clearNum / 1024,
                                                                               clearNum))
# for debug string
# time.sleep(3)
