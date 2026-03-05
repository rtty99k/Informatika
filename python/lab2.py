# TODO Найдите количество книг, которое можно разместить на дискете

size = 1.44
pages = 100
line_page = 50 #вводим все данные
symbol_line = 25
keep = 4

size_byte = size * 1024 ** 2 #размер дискеты в байтах
all_symbol = pages * line_page * symbol_line * keep #общее число символов в книге
book = size_byte // all_symbol #находим число книг
print("Количество книг, помещающихся на дискету:", int(book)) #написал int чтобы выводило целое число
