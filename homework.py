import main


def way_to_course():
    with open('main.py') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
    return cook_book


def closer_and_closer(dishes, persons):
    shop_list = {}
    for dish in dishes:
        for ingridient in main.cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= persons
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))

def make_shop_list():
    persons = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = closer_and_closer(dishes, persons)
    print_shop_list(shop_list)

a = make_shop_list()
print(a)

import os

def compile_files(files_list):
    data = {}
    for file in files_list:
        with open(file, encoding="utf-8") as f:
            file_data = f.readlines()
            data[len(file_data)] = (file, " ".join(file_data))

    data = dict(sorted(data.items()))

    with open("result_data.txt", "w", encoding="utf-8") as new_file:
        for key, value in data.items():
            new_file.write(f"{value[0]} \n")
            new_file.write(f"{key} \n")
            new_file.write(f"{value[1]} \n")


files = ["1.txt", "2.txt", "3.txt"]
files = [os.path.join(os.getcwd(), file) for file in files]
compile_files(files)
