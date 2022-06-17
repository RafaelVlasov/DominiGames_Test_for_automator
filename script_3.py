file = open("/Users/rafael.vlasov/Desktop/Russian-Nouns.txt", 'r', encoding='utf-8')  # открываем файл
words_list = file.readlines()  # считываем все строки в переменную
# создаём словарь, присваиваем ключам буквы русского алфавита, значения нулевые
letters_dict = {"а": 0, "б": 0, "в": 0, "г": 0, "д": 0, "е": 0, "ё": 0, "ж": 0, "з": 0, "и": 0, "й": 0, "к": 0, "л": 0, "м": 0, "н": 0, "о": 0, "п": 0, "р": 0, "с": 0, "т": 0, "у": 0, "ф": 0, "х": 0, "ц": 0, "ч": 0, "ш": 0, "щ": 0, "ъ": 0, "ы": 0, "ь": 0, "э": 0, "ю": 0, "я": 0}

for word in words_list:  # обходим слова
    for letter in word:  # обходим буквы слова
        if letter.lower() in letters_dict:  # проверяем есть ли ключ в словаре соответствующий букве
            letters_dict[letter.lower()] += 1  # если да, то добавляем к значению ключа единицу

letters_dict = dict(sorted(letters_dict.items(), key=lambda x: x[1]))  # сортируем словарь
letters_dict = {k: v for k, v in reversed(list(letters_dict.items()))}  # разворачиваем словарь

for keys, values in letters_dict.items():  # обходим развёрнутый словарь и выводим в консоль ключи и значения
    print(keys, "-", values)