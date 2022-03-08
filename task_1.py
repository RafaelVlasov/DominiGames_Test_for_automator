# Скрипт для приведения папок и файлов выбранной директории к нижнему регистру,
# а также изменение кодировки файлов на "utf-8"

import os
import chardet

path = input('введите путь к директории, которую необходимо обработать, и нажмите ENTER: ')
# добавляем в переменную директорию которую необходимо обработать


def encoding_files(filename):  # функция для изменения кодировки на 'utf-8'
    with open(filename, "rb") as file:
        text = file.read()
        enc = chardet.detect(text).get("encoding")  # проверка типа кодировки текста
        if enc and enc.lower() != "utf-8":
            try:
                text = text.decode(enc)
                text = text.encode("utf-8")
                with open(filename, "wb") as f:
                    f.write(text)
                    print(u"%s сконвертирован." % filename)
            except:
                print(u"Ошибка в имени файла: название содержит русские символы.")
        else:
            print(u"Файл %s находится в кодировке %s и не требует конвертирования." % (filename, enc))


def rename(directorys):  # функция для перевода в нижний регистр файлов и папок
    for i in os.listdir(directorys):
        old_name = os.path.join(directorys, i)
        new_name = os.path.join(directorys, i.lower())
        os.rename(old_name, new_name)


def enumeration(path):  # функция для рекурсивного обхода всех файлов и папок директории
    rename(path)  # вызов функции перевода регистра файлов и папок в директории
    for i in os.listdir(path):
        if os.path.isfile(path + '/' + i):
            encoding_files(path + '/' + i)  # вызов функции изменения кодировки
        if os.path.isdir(path + '/' + i):
            enumeration(path + '/' + i)


enumeration(path)
