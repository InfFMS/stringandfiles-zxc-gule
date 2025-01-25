# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
p = ['.','—']
with open('task1.txt','r',encoding='utf-8') as f:
    a=f.readlines()
    b=len(a)
    c=0
    d=0
    for line in a:
        line=''.join(c for c in line if c not in p)
        word=line.split()
        c+=len(word)
        d+=len(line)
    print(a)
    print('колво строк:',b)
    print('колво слов:',c)
    print('колво символов:',d)