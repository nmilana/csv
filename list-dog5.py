import os
import time
import random


_in = "list"
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

    dog = ''
    dog5 = ''
    i = 1
    for name in f:
        dog += '@' + name[:-1] + ' '
        # print(dog)
        if not (i % 5):
            dog5 += dog[:-1] + '\n'
            dog = ''
        i += 1
    dog5 += dog[:-1] + '\n'

    f = open(f"out/{_in}/{fl[:-4]}/dog5.txt", "w", encoding='utf-8')
    f.write(f'{dog5}')
    f.close()
