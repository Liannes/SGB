import requests
import json


def search(fio, date, doc, passw):  # Поиск в базе ФНС
    token = '94c148150f273bab8047dbbde0b324796e52433b'
    r = requests.get('https://api-fns.ru/api/innfl?fam=%s&nam=%s&otch=%s&bdate=%s&doctype=%s&docno=%s&key=%s'
                     % (fio[0], fio[1], fio[2], date, doc, passw, token))
    data = r.json()
    with open('response.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file)


def read(fio, date, passw):  # Считывание данных и вывод
    with open('response.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)

    if len(data) == 2:
        print("\n" + data.get('error'))
    else:
        inn = data.get('items')[0].get('ИНН')
        print("\nФИО: %s %s %s \n"
              "Дата рождения: %s\nПаспорт: %s\nИНН: %s" % (fio[0], fio[1], fio[2], date, passw, inn))


def info():  # Ввод данных
    with open('text.txt', 'r', encoding='UTF-8') as file:
        info_search = file.readlines()
    fio = input("Введите полное ФИО: ").split()
    date = input("Введите дату рождения: ")
    print("Выберите документ:")
    for i in info_search:
        print(i)
    doc = input("Введите документ: ")
    passw = input("Введите номер документа: ")
    search(fio, date, doc, passw)
    read(fio, date, passw)


info()
input()