user = [
    {'login': 'User',
     'password': 'user1',
     'role': 'user', ## user[0]['cart'].append('gfdsgdf)
     'cart': []},
    {'login': 'Admin',
     'password': 'admin1',
     'role': 'admin'},
]
flowers = [
    {'title': 'Розы','price': 90},
    {'title': 'Орхидеи', 'price': 60},
    {'title': 'Хризантемы', 'price': 50},
    {'title': 'Пионы', 'price': 70},
    {'title': 'Тюльпаны', 'price': 50},
    {'title': 'Гортензии', 'price': 40},
]

def Adminmenu():
    print("Вы вошли как админ.")
    print("Меню действий:\n0. Выйти с роли админа\n1. Добавить новый товар\n"
          "2. Удалить товар\n3. Просмотреть список пользователей")
    while(True):
        act = int(input("Ваше действие: "))
        match(act):
            case 0:
                Checkuser()
                break
            case 1:
                newprod = str(input("Введите название нового товара: "))
                newprice = str(input("Введите его цену: "))
                flowers.append(newprod, newprice)
            case 2:
                print()
            case 3:
                print()

def Usermenu(login):
    print("Вы вошли как пользователь.")
    print("Меню действий:\n0. Выйти из учётной записи\n1. Просмотреть каталог товаров\n"
          "2. Поиск товара по цене\n3. Добавить товар в корзину\n4. Посмотреть корзину")
    while(True):
        act = int(input("Ваше действие: "))
        match(act):
            case 0:
                Checkuser()
                break
            case 1:
                print("Товары, присутсвующие в наличии:")
                j = 1
                for i in flowers:
                    print(f"{j}. {i['title']}, {i['price']} рублей")
                    j += 1
            case 2:
                ot = int(input("От скольки рублей будет поиск: "))
                do = int(input("До скольки: "))
                result = filter(lambda x: ot <= x['price'] <= do, flowers)
                for i in result:
                    print(f"{i['title']}, {i['price']} рублей")
            case 3:
                choice = int(input("Введите номер цветов, которые хотите купить: ")) - 1
                colvo = int(input('Введите количество: '))
                answer = input(f'Хотите добавить в корзину {flowers[choice]['title']} за '
                               f'{flowers[choice]['price'] * colvo} рублей? (Да/Нет) : ')
                if answer == 'Да':
                    for d in user:
                        if d['login'] == login:
                            d['cart'].append({'Название': flowers[choice]['title'],
                                                'количество': colvo, 'цена': flowers[choice]['price'] * colvo})
                else:
                    print("Отмена покупки.")
            case 4:
                for d in user:
                    if d['login'] == login:
                        if len(d['cart']) == 0:
                            print("Корзина пуста.")
                        else:
                            for i in user[0]['cart']:
                                print(i)


def Checkuser():
    print('Здравствуйте! Добро пожаловать в цветочный магазин. Для начала, ввойдите в свою учётную запись:')
    login = input("Введите свой логин: ")
    password = input("Введите пароль: ")
    for i in user:
        if i['login'] == login:
            if i['password'] == password:
                if i['role'] == 'admin':
                    Adminmenu()
                    break
                else:
                    Usermenu(login)
                    break
    print("Неправильный логин или пароль")
    Checkuser()

Checkuser()