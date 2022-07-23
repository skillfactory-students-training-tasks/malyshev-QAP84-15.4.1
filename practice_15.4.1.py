symbol_dict = {33: None, 34: None, 35: None, 36: None, 37: None, 38: None, 39: None, 40: None, 41: None, 42: None,
               43: None, 44: None, 45: None, 46: None, 47: None, 58: None, 59: None, 60: None, 61: None, 62: None,
               63: None, 64: None, 91: None, 92: None, 93: None, 94: None, 95: None, 96: None, 126: None, 48: None,
               49: None, 50: None, 51: None, 52: None, 53: None, 54: None, 55: None, 56: None, 57: None}

def rus_alph(string):
    alphabet = ("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    for char in string:
        if char in alphabet:
            return True
        else:
            return False
def eng_alph(string):
    alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for char in string:
        if char in alphabet:
            return True
        else:
            return False
def sort_str(string):
    if len(string) > 3:
        return string

name_file = input("Введите имя файла: ")

with open(name_file +".txt", 'r', encoding='utf8') as data:

    text_file = data.read()
    text_file = text_file.split()
    text_lenght = len(text_file)
    eng_max_symbol_str = ""
    word_dict = {}
    word_dict2 = {}
    i = 0
    while i < text_lenght:
        temp_str = (text_file[i])
        temp_str = temp_str.translate(symbol_dict)
        if eng_alph(temp_str) or rus_alph(temp_str):
            if len(temp_str) > 3:
                word_dict[temp_str] = text_file.count(temp_str)
                word_dict2[text_file.count(temp_str)] = temp_str
        if eng_alph(temp_str):
            if len(temp_str) > len(eng_max_symbol_str):
                eng_max_symbol_str = temp_str
            else:
                eng_max_symbol_str = eng_max_symbol_str
        i += 1

    print("Наиболее длинное слово на английском языке: " + eng_max_symbol_str)
    print("Наиболее часто встречающееся из тех, что имеют размер более трех символов: " + word_dict2.get(max(word_dict2.keys())))

