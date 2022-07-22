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

def count_lines(file, chunk_size=1<<13):
    with open(file) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

ten = count_lines('1.txt')
twenty = count_lines('2.txt')
thurty = count_lines('3.txt')

one = open('1.txt')
two = open('2.txt')
three = open('3.txt')

first = one.read
second = two.read
thurd = three.read

if ten > twenty and ten > thurty and twenty > thurty:
    print(first)
    print(second)
    print(thurd)
if ten > twenty and ten > thurty and twenty < thurty:
    print(first)
    print(thurd)
    print(second)
if twenty > ten and ten > thurty and twenty > thurty:
    print(second)
    print(first)
    print(thurd)
if twenty > ten and ten < thurty and twenty > thurty:
    print(second)
    print(thurd)
    print(first)
if ten > twenty and ten < thurty and twenty < thurty:
    print(thurd)
    print(first)
    print(second)
if ten < twenty and ten < thurty and twenty < thurty:
    print(thurd)
    print(second)
    print(first)
