#**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#    **Вывод:** Парам пам-пам  
#text=input("Введите стих: ")
text='пара-ра-рам рам-пам-папам па-ра-па-да ру-ру-рам-рам'    
text=list(text.split())
print(text)

text=list(map(lambda x: list(x) ,text))
voice=['у','е','ы','а','о','э','я','и','ю']
print(text)

res=list()
for i in range (len(text)):
    res.append(len(list(filter(lambda x:x in voice,text[i]))))
    
print(res)
if len(set(res))==1:
    print("Парам пам-пам  ")
else:
    print("Пам парам  ")