import os
import re


_in = "mix"

lst_d = os.listdir(f"in/{_in}")
l = len(lst_d)
print(f'{l} files {lst_d} in "in/{_in}" folder')


pattern = r'[^0-9a-zA-Zа-яА-я_]'

for fl in lst_d:

    lst_out = os.listdir(f"out/{_in}")
    if f'{fl[:-4]}' not in lst_out:
        print(f"==Creating 'out/{_in}/{fl[:-4]}' folder==")
        os.mkdir(f"out/{_in}/{fl[:-4]}")

    with open(f'./in/{_in}/{fl[:-4]}.txt', 'rt', encoding='utf-8') as file:
        tags_raw = file.read()

    list_tags = "".join("".join(tags_raw.splitlines()).split('#')).split(' ')
    # print(list_tags)
    print(len(list_tags))
    # print('--------------------------')
    set_tags = list(set(list_tags))[1:]
    print(len(set_tags))
    # print(set_tags)

    i = 1
    j = 1
    tag25 = ''
    for item in set_tags:
        tag25 += re.sub(pattern, '', item) + '\n'
        if not i % 25:
            with open(f"out/{_in}/{fl[:-4]}/{fl[:-4]}_{str(j).zfill(2)}.txt", "w", encoding='utf-8') as file:
                file.write(f'{tag25}')
            tag25 = ''
            j += 1
        i += 1

    # print(tag25)

    if tag25 != '':
        with open(f"out/{_in}/{fl[:-4]}/{fl[:-4]}_{str(j).zfill(2)}.txt", "w", encoding='utf-8') as file:
            file.write(f'{tag25}')   

