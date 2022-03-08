# Скрипт для сравнения полей xlsx файла с полями файлов xlm и plist
# Файлы для сравнения необходимо разместить в папке расположения скрипта

from openpyxl import *
import xml.dom.minidom as minidom
import os

book = open('DominiGames Test  Sheet.xlsx', read_only=True)  # открывает эксель таблицу
sheet = book.active
plist_UniversalF2P = {}  # первый словарь для сохранения в него 1 и 2 столбца эксель и сравнения с .plist файлом
cells = sheet['A2': 'B100']  # диапазон ячеек взяв крайнюю границу с запасом,
#  либо можно скорректировать эту границу и задавать её через input() из консоли

for keys, values in cells:
    plist_UniversalF2P[keys.value] = str(values.value)

purchase = {}  # второй словарь для сохранения в него 3 и 4 столбца эксель и сравнения с .xml файлом
cells = sheet['C2':'D100']  # обновляем диапазон для заполнения второго словаря взяв крайнюю границу с запасом

for keys, values in cells:
    purchase[keys.value] = str(values.value)

file_dominiap = minidom.parse('DominiIAP.xml')  # анализируем .xml файл
node = file_dominiap.documentElement
items_key = file_dominiap.getElementsByTagName('ProductID')  # собираем ключи по тагу
items_value = file_dominiap.getElementsByTagName('analytics_event_name')  # собираем значения по тагу

keys_list = []
values_list = []

for elem in items_key:
    keys_list.append(elem.firstChild.data)

for elem in items_value:
    values_list.append(elem.firstChild.data)

# чтобы не потерять ключи из-за разности длинны списков если в файле есть не все значения, выравниваем количество
# элементов значениями 'No value'

while len(keys_list) != len(values_list):
    values_list.append('No value')

dominiap_dict = dict(zip(keys_list, values_list))  # создаём словарь для заполнения ключей и значений из .xml файла

file_info = 'Info.plist'
part_name_file = file_info.split('.')
old_name = os.path.join(file_info)
new_name = os.path.join(part_name_file[0] + '.xml')
os.rename(old_name, new_name)  # меняем расширение файла для дальнейшего парсинга данных

doc_info = minidom.parse(new_name)
node = doc_info.documentElement
items_key = doc_info.getElementsByTagName('key')
items_value = doc_info.getElementsByTagName('string')
keys_list = []
values_list = []

for elem in items_key:
    keys_list.append(elem.firstChild.data)

for elem in items_value:
    values_list.append(elem.firstChild.data)

while len(keys_list) != len(values_list):
    values_list.append('No value')

info_dict = dict(zip(keys_list, values_list))  # создаём словарь для заполнения ключей и значений из .plist файла

for keys, values in plist_UniversalF2P.items():
    if keys in info_dict:
        if plist_UniversalF2P[keys] != info_dict[keys]:
            print('ERROR! Key', keys, 'has the wrong value in Info.plist', plist_UniversalF2P[keys], '!=', info_dict[keys])

for keys, values in purchase.items():
    if keys in dominiap_dict:
        if purchase[keys] != dominiap_dict[keys]:
            print('ERROR! Key', keys, 'has the wrong value in DominiIAP.xml', purchase[keys], '!=', dominiap_dict[keys])

part_name_file = new_name.split('.')
old_name = os.path.join(new_name)
new_name = os.path.join(part_name_file[0] + '.plist')
os.rename(old_name, new_name)  # возвращаем расширение файла обратно в .plist
