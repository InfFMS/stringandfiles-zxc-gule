# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
from collections import Counter
a=[]
with open('task3.txt','r',encoding='utf-8') as f:
    b=f.read()
    c=b.lower()
    a=c.split()
res=a.sort()
d=Counter(a)
l=sorted(d.items())
with open('new_file3.txt','w',encoding='utf-8') as new_file:
    for i,q in l:
        new_file.write(f"{i}:{q}\n")