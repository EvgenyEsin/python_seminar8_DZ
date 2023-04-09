def show_data(file):
    '''1 Выводит информацию из справочника'''
    with open(file, 'r', encoding='utf-8') as f:
        print(f.read())
        

def add_data(file, tel_data):
    '''2 Добавляет информацию в справочник'''
    fio=input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        tel_data.append(fio + ' - ' + tel_number) # формируем список ФИО и телефонов
        f.write(fio + ' - ' + tel_number + '\n')
    print('Информация добавлена.')
    return tel_data
    

def find_data(file):
    '''3 Осуществляет поиск по справочнику'''
    data = input('Введите данные для поиска: ').lower()
    srch_data(file, data, srch_list=[])
         

def edited_data(file, tel_data, srch_list=[]):
    '''4 Редактирует данные'''
    data= input('Введите данные для редактирования: ').lower()
    srch_data(file, data, srch_lis=[])
    if len(srch_list)==1:
        edit_num = 1
    else:
        edit_num = int(input('Выберите строку, которую хотите изменить: '))
        print(f'Вы выбрали: {srch_list[edit_num-1]}')
    for i in range(len(tel_data)-1):
        if srch_list[edit_num-1] in tel_data[i]:
            index = i # запоминаем индекс в tel_data для замены
    fio=input('Введите новое ФИО: ')
    tel_number = input('Введите новый номер телефона: ')
    tel_data[index]=(fio + ' - ' + tel_number + '\n')
    with open(file, 'w', encoding='utf-8') as f:
        for i in tel_data:
            f.write(i)
    return print('Справочник изменен успешно.'), f


def delete_data(file, tel_data, srch_list=[]):
    '''5 Удаляет данные'''
    data= input('Введите данные для удаления: ').lower()
    srch_data(file, data, srch_list=[])
    if len(srch_list)==1:
        edit_num = 1
    else:
        edit_num = int(input('Выберите строку, которую хотите удалить: '))
    d=input('Вы точно хотите удалить? (нажмите 5 для удаления))\n')
    if d != '5':
        return print('Удаление отменено')
    else:
        for i in range(len(tel_data)-1):
            if srch_list[edit_num-1] in tel_data[i]:
                tel_data.pop(i)
    with open(file, 'w', encoding='utf-8') as f:
        for i in tel_data:
            f.write(i)
    return print('Справочник изменен успешно.'), f


def srch_data(file, data, srch_list=[], index=1):
    '''дополнительная функция для поиска'''
    with open(file, 'r', encoding='utf-8') as f:
        book = f.readlines()
        for line in book:
            if data in line.lower():
                srch_list.append(line)
                print(f'{index}. {srch_list[index-1]}', end='')
                index+=1
        if index > 1:
            return srch_list
        else:
            print('Такой информации не найдено.')


def fill_data(file, tel_data=[]):
    '''доплнительная функция для заполнения всего списка'''
    with open(file, 'r', encoding='utf-8') as f:
        book = f.readlines()
        for line in book:
            tel_data.append(line)
        return tel_data
        