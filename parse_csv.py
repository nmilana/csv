import os
from selenium import webdriver
# import selenium.webdriver.support.expected_conditions as EC
import time
import random

# log/pass
lst_d = os.listdir("in")
l = len(lst_d)
print(f'{l} files {lst_d}')

for fl in lst_d:
    f = open(f'in/{fl}', "r", encoding='utf-8')
    os.mkdir(f"out/{fl[:-4]}")
    all = []
    _set = set()
    dic = {}
    j = 0
    for line in f:
        j += 1
        if j == 1: continue
        all.append(line[1:-2].split('";"'))
        el = all[-1][1::2]
        _set.add(el[0])
        if el[0] in dic:
            dic[el[0]] += f' {all[-1][3]}'
        else:
            dic[el[0]] = f'{all[-1][3]}'

    lst = ''
    dog = ''
    dog5 = ''
    dic_csv = ''
    i = 0
    for name in _set:
        lst += name + '\n'
        dog += '@' + name + ' '
        # print(dog)
        if not (i % 5) and i:
            dog5 += dog[:-1] + '\n'
            dog = ''
        dic_csv += f'"{name}";"{dic[name]}"\n'
        i += 1

    f = open(f"out/{fl[:-4]}/list.txt", "w", encoding='utf-8')
    f.write(f'{lst}')
    f.close()

    f = open(f"out/{fl[:-4]}/dog5.txt", "w", encoding='utf-8')
    f.write(f'{dog5}')
    f.close()

    f = open(f"out/{fl[:-4]}/dic.txt", "w", encoding='utf-8')
    f.write(f'{dic}')
    f.close()

    f = open(f"out/{fl[:-4]}/dic.csv", "w", encoding='utf-8')
    f.write(f'{dic_csv}')
    f.close()  