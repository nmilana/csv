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
print(f'{l} files {lst_in} in "in" folder')


lst_d = os.listdir(f"in/{_in}")
l = len(lst_d)
print(f'{l} files {lst_d} in "in/list" folder')


for fl in lst_d:
    f = open(f'in/{_in}/{fl}', "r", encoding='utf-8')

    lst_out = os.listdir(f"out/{_in}")
    if f'{fl[:-4]}' not in lst_out:
        print(f"Make '{fl[:-4]}' folder in out/{_in} folder")
        os.mkdir(f"out/{_in}/{fl[:-4]}")

    dog1 = ''
    dog5 = ''
    dog10 = ''
    i = 1
    for name in f:
        print(name[:-1])
        dog1 += '@' + name[:-1] + '\n'
        dog5 += '@' + name[:-1] + (' ' if i % 5 else '\n')
        dog10 += '@' + name[:-1] + (' ' if i % 10 else '\n')
        i += 1
    dog5 = dog5[:-1] + '\n'
    print(f'\n{dog5}')
    dog10 = dog10[:-1] + '\n'
    # print(dog10)

    f = open(f"out/{_in}/{fl[:-4]}/dog1.txt", "w", encoding='utf-8')
    f.write(f'{dog1}')
    f.close()

    f = open(f"out/{_in}/{fl[:-4]}/dog5.txt", "w", encoding='utf-8')
    f.write(f'{dog5}')
    f.close()

    f = open(f"out/{_in}/{fl[:-4]}/dog10.txt", "w", encoding='utf-8')
    f.write(f'{dog10}')
    f.close()