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

def Sorted(elements, text):
    print(text)
    for elements in elements:
        for key, value in elements.items():
            print(f"{key}: {value}", end=" ")
            if key == "price":
                print()

def Sorting(login):
    print("Меню сортировки или фильтрации:\n0. Выйти из меню\n1. Сортировка по цене от большего к меньшему"
          "\n2. Сортировка по цене от меньшего к большему\n3. Фильтрация цены <от> и <до>")
    while True:
        while True:
            try:
                choice = int(input("Ваш выбор в меню сортировок: "))
                if choice > 3:
                    print("--Число должно быть меньше 4--")
                elif choice < 0:
                    print("--Число должно быть не меньше 0-- ")
                else:
                    break
                break
            except ValueError:
                print("--Можно ввести только числа--")
        match choice:
            case 0:
                Usermenu(login)
            case 1:
                elements = sorted(flowers, key=lambda flower: flower["price"])
                Sorted(text="Цветы по цене от большего к меньшему:",
                       elements=sorted(flowers, key=lambda flower: flower["price"], reverse = True))
            case 2:
                elements = sorted(flowers, key=lambda flower: flower["price"])
                Sorted(text="Цветы по цене от меньшего к большему:",
                        elements=sorted(flowers, key=lambda flower: flower["price"]))
            case 3:
                while True:
                    try:
                        ot = int(input("От скольки рублей будет поиск: "))
                        if ot < 0:
                            print("--Данное значение должно быть больше 0--")
                        else:
                            break
                    except ValueError:
                        print("--Можно ввести только числа--")
                while True:
                    try:
                        do = int(input("До скольки: "))
                        if do < ot:
                            print("--Данное значение должно быть больше ранее введённого--")
                        else:
                            break
                    except ValueError:
                        print("--Можно ввести только числа--")
                result = filter(lambda x: ot <= x['price'] <= do, flowers)
                print("Товары, соответствующие введённым критериям:")
                print("--------------------------------------")
                for i in result:
                    print(f"{i['title']}, {i['price']} рублей")
                print("--------------------------------------")

def Adminmenu():
    print("Вы вошли как админ.")
    print("Меню действий:\n0. Выйти с роли админа\n1. Добавить новый товар\n"
          "2. Удалить товар")
    while True:
        while True:
            try:
                act = int(input("Ваше действие: "))
                if act > 2:
                    print("--Число должно быть меньше 3--")
                elif act < 0:
                    print("--Число должно быть не меньше 0-- ")
                else:
                    break
            except ValueError:
                print("--Можно ввести только числа--")
        match act:
            case 0:
                Checkuser()
                break
            case 1:
                while True:
                    try:
                        newprod = str(input("Введите название нового товара: "))
                        break
                    except ValueError:
                        print("--Можно записать только слово--")
                while True:
                    try:
                        newprice = int(input("Введите его цену: "))
                        break
                    except ValueError:
                        print("--Можно ввести только цифры--")
                print("--Хотите добавить новый товар?")
                while True:
                    answer = input("Да/Нет: ")
                    if answer in ['Да', 'дА', 'да']:
                        newsl = {'title': newprod, 'price': newprice}
                        flowers.append(newsl)
                        print("--Товар был успешно добавлен в каталог.")
                        break
                    elif answer in ['Нет', 'НЕт', 'НЕТ', 'нЕТ', 'неТ', 'НеТ', 'нет']:
                        print("--Добавление товара отменено.")
                        break
                    else:
                        print("--Введите точно команду да или нет--")
            case 2:
                print("--------------------------------")
                j = 1
                for i in flowers:
                    print(f"{j}. {i['title']}, {i['price']} рублей")
                    j += 1
                print("--------------------------------")
                while True:
                    try:
                        delz = int(input("Введите номер товара, который хотите удалить: ")) - 1
                        if delz < 0:
                            print("--Число должно быть не меньше 0--")
                        elif delz > j:
                            print("--Число должно быть меньше" + (j +1) + "--")
                        else:
                            break
                    except ValueError:
                        print("--Можно ввести только числа--")
                print("--Хотите удалить данный товар?")
                while True:
                    answer = input("Да/Нет: ")
                    if answer in ['Да', 'дА', 'да']:
                        flowers.pop(delz)
                        print("--Товар был успешно удалён.")
                        break
                    elif answer in ['Нет', 'НЕт', 'НЕТ', 'нЕТ', 'неТ', 'НеТ', 'нет']:
                        print("--Удаление товара отменено.")
                        break
                    else:
                        print("--Введите точно команду да или нет--")

def Usermenu(login):
    print("Меню действий:\n0. Выйти из учётной записи\n1. Просмотреть каталог товаров\n"
          "2. Поиск товара\n3. Добавить товар в корзину\n4. Посмотреть корзину")
    while True:
        while True:
            try:
                act = int(input("Ваше действие: "))
                if act > 4:
                    print("--Число должно быть меньше 5--")
                elif act < 0:
                    print("--Число должно быть не меньше 0-- ")
                else:
                    break
            except ValueError:
                print("--Можно ввести только цифры--")
        match act:
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
                Sorting(login)
            case 3:
                while True:
                    while True:
                        try:
                            choice = int(input("Введите номер цветов, которые хотите купить: ")) - 1
                            break
                        except ValueError:
                            print("--Можно ввести только числа--")
                    while True:
                        try:
                            colvo = int(input("Введите количество: "))
                            if colvo < 1:
                                print("Можно купить только начиная с 1 цветка!")
                            else:
                                break
                        except ValueError:
                            print("--Можно ввести только числа--")
                    try:
                        print(f'Хотите добавить в корзину {flowers[choice]['title']} за '
                                    f'{flowers[choice]['price'] * colvo} рублей?')
                        break
                    except IndexError:
                        print("Такого товара не существует!")
                while True:
                    answer = input("Да/Нет: ")
                    if answer in ['Да', 'дА', 'да']:
                        for d in user:
                            if d['login'] == login:
                                d['cart'].append({'Название': flowers[choice]['title'],
                                                'количество': colvo,
                                                'цена': flowers[choice]['price'] * colvo})
                                print("Товар был добавлен в корзину!")
                        break
                    elif answer in ['Нет', 'НЕт', 'НЕТ', 'нЕТ', 'неТ', 'НеТ', 'нет']:
                        print("Отмена покупки.")
                        break
                    else:
                        print("--Введите точно команду да или нет--")
            case 4:
                for d in user:
                    if d['login'] == login:
                        if len(d['cart']) == 0:
                            print("Корзина пуста.")
                        else:
                            for i in user[0]['cart']:
                                print(i)
                            print("Желаете ли произвести покупку?")
                            while True:
                                answer = input("Да/Нет: ")
                                if answer in ['Да', 'дА', 'да']:
                                    d['cart'].clear()
                                    print("Спасибо за покупку!")
                                    break
                                elif answer in ['Нет', 'НЕт', 'НЕТ', 'нЕТ', 'неТ', 'НеТ', 'нет']:
                                    break
                                else:
                                    print("--Введите точно команду да или нет--")


def Checkuser():
    print('Здравствуйте! Добро пожаловать в цветочный магазин. Для начала, ввойдите в свою учётную запись: (или нажмите 0, если хотите выйти)')
    login = input("Введите свой логин: ")
    if login == '0':
        print("До свидания!")
        return
    password = input("Введите пароль: ")
    for i in user:
        if i['login'] == login:
            if i['password'] == password:
                if i['role'] == 'admin':
                    Adminmenu()
                    break
                else:
                    print("Вы вошли как пользователь.")
                    Usermenu(login)
                    break
    print("Неправильный логин или пароль")
    Checkuser()

Checkuser()