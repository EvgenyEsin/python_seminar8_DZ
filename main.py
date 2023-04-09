import functions

file = 'book.txt'
tel_data = [] # создали пустой список для телефоннго справочника
num = 1
while num:
    print('1 - показать справочник, 2 - добавить новую запись, 3 - поиск, 4 - изменение записи, 5 - удаление записи')
    mode = int(input())
    if mode == 1:
        functions.show_data(file)
    elif mode == 2:
        functions.fill_data(file, tel_data)
        functions.add_data(file, tel_data)
    elif mode == 3:
        functions.find_data(file)
    elif mode == 4:
        functions.fill_data(file, tel_data)
        functions.edited_data(file, tel_data)
    elif mode == 5:
        functions.fill_data(file, tel_data)
        functions.delete_data(file, tel_data)
    else:
        num = 0
