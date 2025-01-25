# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
new_text=''
c=0
with open('task2.txt','r',encoding='utf-8') as f:
    a=f.read()
    b=a.split(' ')
    for i in range(len(b)):
        if b[i]=='Python':
            b[i]='Питон'
            c+=1
        if b[i]=='\nPython':
            b[i]='\nПитон'
            c+=1
        new_text+=b[i]+' '
    print(new_text)
    print('Всего замен:',c)
with open('gg_net.txt','w',encoding='utf-8') as gg_net:
    gg_net.write(new_text)