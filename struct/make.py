
import os
from local.utils import uread, uopen


def modify_content(text):
    return (text.replace('（', '(')
                .replace('）', ')')
                .replace('，', ',')
                .replace('；', ';'))



content = uread(r'struct.txt')
image_path = 'https://cdn.jsdelivr.net/gh/FrozenCollection/EnglishLearning@main/struct/image/{}'

with uopen(r'words.txt', 'w') as fout:
    word = ''
    flag = False
    for line in content.split('\n'):
        if flag := not flag:
            word = line
            line = '[VIZ-S] ' + line
            fout.write(line + '\t')
        else:
            line = modify_content(line)
            image_file = f"{word}.jpg"
            if not os.path.exists(os.path.join('image', image_file)):
                print(f'warning: image {word} not exists')
            fout.write(line + f'<br><img src="{image_path.format(image_file)}">' + '\n')

