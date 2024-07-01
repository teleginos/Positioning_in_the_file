from functions import custom_write

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('file_info.txt', info)

for elem in result.items():
    print(elem)
