В репозитории три скрипта:

1. Рекурсивно приводит папки и файлы к нижнему регистру, а также переводит все файлы в utf-8.
2. Проверяет поля 2х файлов (plist, xml) на валидность из Excel-документа. Т.е. в файле эксель содержится 2 группы ключей и значений. Скрипт собирает две пары ключей и значений, после чего ищет ключи в файле plist и в файле xml, сравнивая значения идентичных ключей. Если в файлах plist или xml содержится ключ, которого нет в эксель или ключи и значения в обоих файлах совпадают, игнорирует такие строки. Если ключи идентичны, а значения различны, выводит ошибку в консоль.
3. Считает количество букв в заранее скаченном файле (.txt-файл представляет собой список русских слов). Выводит список букв русского словаря с указанием их количества в обрабатываемом файле.  Вывод отсортировывается от большего количества к меньшему. 
