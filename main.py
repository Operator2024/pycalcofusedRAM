# -*- coding: utf-8 -*-

import os,sys,subprocess,time
import re


variab = input("Enter process name as 'tasklist': ")
proc = subprocess.Popen(["tasklist",'/FI',"IMAGENAME eq {0}".format(variab),"/FO","TABLE","/NH"],stdout=subprocess.PIPE,shell=True)
data = proc.stdout.readlines()
clearNum = 0
for i in range(1,len(data)):
    # получаем число в виде строки и убираем запятую.
    Num = re.sub(r"\s+", "||", data[i].decode("cp866").replace("\s", "")).split("||")[4]
    clearNum +=int(re.sub(r",","",Num))


with open(f'{variab[0:len(variab)-4]}.txt',"w") as file:
    file.write("Memory is busy process: {0} bytes, {1} megabytes, {2} kilobytes \nTotal process: {3}".format(
        clearNum * 1024,clearNum/1024, clearNum,len(data)-1))

print("Memory is busy process: {0} bytes, {1} megabytes, {2} kilobytes".format(clearNum * 1024,clearNum/1024, clearNum))

# c = wmi.WMI ()
# allocateMemory = []
# for process in c.Win32_Process (Name="epic.exe".format(input('Enter process name as "tasklist": '))):
#
#     allocateMemory.append(int(process.WorkingSetSize))
#
# print("Memory is busy process: {0} bytes, {1} megabytes, {2} kilobytes".format(sum(allocateMemory),sum(allocateMemory)/1048576,sum(allocateMemory)/1024))

time.sleep(10)

