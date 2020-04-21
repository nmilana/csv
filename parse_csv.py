import os
import time
import random


_in = "csv"
lst_in = os.listdir(f"in")
l = len(lst_in)
if _in not in lst_in:
    print(f"Don't found '{_in}' folder")
    os.mkdir(f"in/{_in}")
    quit()
print(f'{l} files {lst_in}')




lst_d = os.listdir(f"in/{_in}")
l = len(lst_d)
print(f'{l} files {lst_d}')


for fl in lst_d:
    f = open(f'in/{_in}/{fl}', "r", encoding='utf-8')

    lst_out = os.listdir(f"out/{_in}")
    if f'{fl[:-4]}' not in lst_out:
        print(f"Make '{fl[:-4]}' folder in out/{_in} folder")
        os.mkdir(f"out/{_in}/{fl[:-4]}")

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
    i = 1
    for name in _set:
        lst += name + '\n'
        dog += '@' + name + ' '
        # print(dog)
        if not (i % 5):
            dog5 += dog[:-1] + '\n'
            dog = ''
        dic_csv += f'"{name}";"{dic[name]}"\n'
        i += 1
    dog5 += dog[:-1] + '\n'

    f = open(f"out/{_in}/{fl[:-4]}/list.txt", "w", encoding='utf-8')
    f.write(f'{lst}')
    f.close()

    f = open(f"out/{_in}/{fl[:-4]}/dog5.txt", "w", encoding='utf-8')
    f.write(f'{dog5}')
    f.close()

    f = open(f"out/{_in}/{fl[:-4]}/dic.txt", "w", encoding='utf-8')
    f.write(f'{dic}')
    f.close()

    f = open(f"out/{_in}/{fl[:-4]}/dic.csv", "w", encoding='utf-8')
    f.write(f'{dic_csv}')
    f.close()
