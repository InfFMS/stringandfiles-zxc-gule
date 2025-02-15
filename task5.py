# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
with open("task5.txt","r",encoding="utf-8") as f:
    a=f.read()
b=a.split()
print(b)
c=""
h=0
p=['.',',','!','?']
for i in b:
    if i[0] in p:
        i=i[1:]
    if i[-1] in p:
        i=i[:-1]
    n = len(i)
    if n>h:
        h=n
        c=i
long=(f"Самое длинное слово: {c}\nЕго длина: {h}")
with open("result5.txt","w",encoding="utf-8") as g:
    g.write(long)
print(c)
print(h)