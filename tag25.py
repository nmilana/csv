import re

_in = "mix"
with open('./in/mix/tags.txt', 'rt', encoding='utf-8') as file:
    tags_raw = file.read()

list_tags = "".join("".join(tags_raw.splitlines()).split('#')).split(' ')
print(list_tags)
print(len(list_tags))
print('--------------------------')
set_tags = list(set(list_tags))[1:]
print(len(set_tags))
print(set_tags)


i = 1
tag25 = ''
for item in set_tags:
    tag25 += item + '\n'
    if not i % 25:
        with open(f"out/{_in}/tag25_{str(int(i / 25)).zfill(2)}.txt", "w", encoding='utf-8') as file:
            file.write(f'{tag25}')
        tag25 = ''
    i += 1

# print(tag25)

if tag25 != '':
    with open(f"out/{_in}/tag25_{str(int(i / 25) + 1).zfill(2)}.txt", "w", encoding='utf-8') as file:
        file.write(f'{tag25}')   

