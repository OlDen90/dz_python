vocabulary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(number):
    print(f"{vocabulary.get(number)}")


# Добавление в словарь новых элементов (вне ДЗ):
# vocabulary_after_ten = {"eleven": "одиннадцать"}
# vocabulary.update(vocabulary_after_ten)

num_translate("one")
num_translate("eight")
num_translate("eleven")
