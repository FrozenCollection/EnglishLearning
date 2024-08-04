
import os
from local.utils import uread, uopen


def modify_content(text):
    return (text.replace('（', '(')
                .replace('）', ')')
                .replace('，', ',')
                .replace('；', ';'))



content = uread(r'item.txt')

with uopen(r'words.txt', 'w') as fout:
    word = ''
    flag = False
    for line in content.split('\n'):
        if flag := not flag:
            word = line
            line = '[VIZ-N] ' + line
            fout.write(line + '\t')
        else:
            line = modify_content(line)
            image_file = f"{word}.jpg"
            if not os.path.exists(image_file):
                print(f'warning: image {word} not exists')
            fout.write(line + f'<br><img src="VIZ-N/{image_file}">' + '\n')

