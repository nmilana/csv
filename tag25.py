import re

_in = "mix"
with open('./input/mix/tags.txt', 'rt', encoding='utf-8') as file:
    tags_raw = file.read()

list_tags = "#".join("".join(tags_raw.splitlines()).split('#')).split(' ')
print(len(list_tags))

set_tags = set(list_tags)
print(len(set_tags))


i = 1
tag25 = ''
for item in set_tags:
    tag25 += item + ' '
    if not i % 25:
        with open(f"out/{_in}/tag25_{str(int(i / 25)).zfill(2)}.txt", "w", encoding='utf-8') as file:
            file.write(f'{tag25}')
        tag25 = ''
    i += 1

# print(tag25)

if tag25 != '':
    with open(f"out/{_in}/tag25_{str(int(i / 25) + 1).zfill(2)}.txt", "w", encoding='utf-8') as file:
        file.write(f'{tag25}')   

