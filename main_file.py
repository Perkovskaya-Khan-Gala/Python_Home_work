"""Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
 """
import shutil

def create_csv(filename: str):
    with open(filename, 'w', encoding='utf-8') as fin:
        for i in range(20):
            fin.write(input("Введите Фамилию, Имя, Телефон и Описание чере запятую:")+'\n')

def show_menu() -> int:
    print("\nМеню:\n"
    "1. Отобразить весь справочник\n"
    "2. Найти абонента по фамилии\n"
    "3. Найти абонента по номеру телефона\n"
    "4. Добавить абонента в справочник\n"
    "5. Сохранить справочник в текстовом формате\n"
    "6. Закончить работу")
    choice = int(input("Выберите необходимое действие:"))
    return choice

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)      
    return data

def printAll():
    listAll=[]
    listAll=read_csv('file.txt')
    for dict in listAll:
        for item in dict:
            print('{}:{}'.format(item,dict[item]))
        print()    

def findUserPhoneNumber(phoneNumber):
    listAll=[]
    listAll=read_csv('file.txt')
    flag=1
    for dict in listAll:
        if int(dict["Телефон"])==phoneNumber:
            for item in dict:
                print('{}:{}'.format(item,dict[item])) 
            flag=0
    return flag                     

def findUserSurname(surname:str):
    listAll=[]
    listAll=read_csv('file.txt')
    flag=1
    for dict in listAll:
        if dict["Фамилия"]==surname:
            for item in dict:
                print('{}:{}'.format(item,dict[item]))
            flag=0
    return flag
        
def addUser(filename: str):
    with open(filename, 'a', encoding='utf-8') as fin:
        fin.write(input("Введите Фамилию, Имя, Телефон и Описание нового абонента через запятую:\n")+'\n')

def saveAsTxt(newName):
    newFile = open(newName, "w+")
    shutil.copyfile('file.txt',newName)
    newFile.close
    print("Файл сохранен")

def makeChoice():
    while True:
        r=show_menu() 
        if r==1:
            printAll()
        elif r==2:
            if findUserSurname(input("Введите фамилию абонента с большой буквы:")):
                print("Такого абонента не существует. Попробуйте еще раз.")
        elif r==3:
            if findUserPhoneNumber(int(input("Введите телефон абонента:"))):
                print("Такого абонента не существует. Попробуйте еще раз.")
        elif r==4:
            addUser('file.txt')
            print("Абонент успешно добавлен")
        elif r==5:
            saveAsTxt(input('Введите имя файла с указанием расширения:'))
        elif r==6:
            break
        print(input("Введите Enter, для возврата в меню"))            


makeChoice()