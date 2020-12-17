class GoodInfo:
    """
    Представляет собой класс в котором находятся три свойства:
        name: str - название товара
        quantity: int - количество
        price: int - цена
    Методы:
        __init__(self, good, price, quantity)
        __str__(self)
        __getitem__(self, key)
    """
    name = None
    quantity = None
    price = None

    def __init__(self, name, price, quantity):
        """
        :param name: str
        :param price: int
        :param quantity: int
        """
        if quantity.isdigit() and price.isdigit():
            self.name = name
            self.quantity = int(quantity)
            self.price = int(price)
        else:
            print('неверный формат! {}'.format(name))

    def __str__(self):
        return '{}: {}руб, {}шт'.format(self.name, self.price, self.quantity)

    def __getitem__(self, key):
        """
        Получает элемент из GoodInfo по индексу
        :param key: int
        :return: class GoodInfo
        """
        if key == 0 or key == 'name':
            return self.name
        elif key == 1 or key == 'price':
            return self.price
        elif key == 2 or key == 'count':
            return self.quantity
        else:
            print('Такого параметра нет - {}'.format(key))


class GoodInfoList:
    """
    good_info_list: str
    Методы:
        __init__(self, good, price, quantity)
        __str__(self)
        __getitem__(self, key)
        read_file(self, file)
        show(self)
        add(self, other)
        remove(self, name)
        get_max_cost(self)
        get_min_cost(self)
        get_min_quantity(self)
        remove_expensive(self)
        sort(self, key='name')
        """
    good_info_list = None

    def __init__(self):
        self.good_info_list = []

    def __str__(self):
        return f'{self.good_info_list}'

    def __getitem__(self, key):
        """
        Получает элемент из списка GoodInfoList по индексу
        :param key: int
        :return: class GoodInfo
        """
        if isinstance(key, int):
            if key >= len(self.good_info_list):
                raise IndexError('{}'.format(key))
            else:
                return self.good_info_list[key]

        else:
            raise AttributeError('{}'.format(key))

    def __len__(self):
        return len(self.good_info_list)

    def read_from_file(self, file):
        """
        Создает GoodInfoList из файла записей формата str:int:int,
        :param file: str
        """
        with open(file, 'r', encoding="utf-8") as data_file:
            data = data_file.readlines()

        for entry in data:
            items = entry.split(":")

            if any(map(lambda good_info:
                       good_info[0] == items[0], self.good_info_list)):
                print(items[0])
                print("Такой товар уже есть!")
            else:

                if len(items) == 3 and items[1].isdigit() \
                        and items[2].replace("\n", "").isdigit():
                    # если вид name:count:cost и count, cost - числа
                    self.add(GoodInfo(items[0],
                                      items[1], items[2].replace("\n", "")))
                else:
                    print('неверный формат {}'.format(items))

    def show(self):
        """
        Выводит элементы списка GoodInfoList
        """
        for good in self.good_info_list:
            print(good)

    def add(self, other):
        """
        Добавляет элемент класса GoodInfo в список, если такого товара еще нет
        :param other: class GoodInfo
        """
        if isinstance(other, GoodInfo):
            if any(map(lambda good_info:
                       good_info[0] == other[0], self.good_info_list)):
                print("Такой товар уже есть!")
            else:
                self.good_info_list.append(other)
        else:
            raise ValueError('{}'.format(other))

    def remove(self, name):
        """
        Удаляет из GoodInfoList объект GoodInfo с указанныи именем
        :param name: str
        """
        for good_info in self.good_info_list:
            if good_info.name == name:
                self.good_info_list.remove(good_info)

    def remove_last(self):
        """
        Удаляет из GoodInfoList последний объект GoodInfo
        """
        del self.good_info_list[-1]

    def get_max_cost(self):
        """
        Возвращает список товаров с макс стоимостью
        :return: list of GoodInfo
        """
        max_cost = 0
        max_cost_list = []

        for good_info in self.good_info_list:
            if good_info.price > max_cost:
                max_cost = good_info.price

        for good_info in self.good_info_list:
            if good_info.price == max_cost:
                max_cost_list.append(str(good_info))

        return '\n' + '\n'.join(max_cost_list)

    def get_min_cost(self):
        """
        Возвращает список товаров с мин стоимостью
        :return: list of GoodInfo
        """
        min_cost = 99999
        min_cost_list = []

        for good_info in self.good_info_list:
            if good_info.price < min_cost:
                min_cost = good_info.price

        for good_info in self.good_info_list:
            if good_info.price == min_cost:
                min_cost_list.append(str(good_info))

        return '\n' + '\n'.join(min_cost_list)

    def get_min_quantity(self):
        """
        Возвращает список товаров с мин количеством
        :return: list of GoodInfo
        """
        min_quantity = 99999
        min_quantity_list = []

        for good_info in self.good_info_list:
            if good_info.quantity < min_quantity:
                min_quantity = good_info.quantity

        for good_info in self.good_info_list:
            if good_info.quantity == min_quantity:
                min_quantity_list.append(str(good_info))

        return '\n' + '\n'.join(min_quantity_list)

    def remove_expensive(self):
        """
        При помощи метода .get_max_cost находит максимальную цену товара
        и удаляет из GoodInfoList все GoodInfo с такой ценой
        """
        max_cost = self.get_max_cost().split(':')[1].split(',')[0] \
            .replace("руб", "").replace(" ", "")

        for good_info in self.good_info_list:
            if good_info.price == int(max_cost):
                self.good_info_list.remove(good_info)

    def __bubble_sort(self, param=0):
        """
        Принимает индексы объектов GoodInfo[0-2]
        и сортирует их в GoodInfoList
        :param key: int, str
        """
        lst = self.good_info_list
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(lst) - 1):
                if lst[i][param] > lst[i + 1][param]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True

    def sort(self, key='name'):
        """
        Принимает на вход строку key = 'name', 'count', 'cost' и применяет
        функцию сортировки по указанному значению
        :param key: str
        """
        if key == 'name':
            self.__bubble_sort(0)
        elif key == 'count':
            self.__bubble_sort(2)
        elif key == 'cost':
            self.__bubble_sort(1)
        else:
            raise AttributeError('{}'.format(key))

    def get_quantity(self):
        count = 0
        for good in self.good_info_list:
            count += good[2]
        return count

    def get_average_price(self):
        count = 0
        for good in self.good_info_list:
            count += good[1]
        return count / len(self.good_info_list)

    def get_std(self):
        """
        Получает среднее отклонение для всех цен товаров
        :return: float
        """
        average = self.get_average_price()
        summ = 0
        for good in self.good_info_list:
            summ += (good.price - average) ** 2

        std = (summ / len(self.good_info_list)) ** .5

        return std


goods_list = GoodInfoList()
goods_list.read_from_file('goods')

max_cost_goods = goods_list.get_max_cost()
min_cost_goods = goods_list.get_min_cost()
min_quantity_goods = goods_list.get_min_quantity()
total_quantity = goods_list.get_quantity()
average_price = goods_list.get_average_price()

print("Общее количество товаров: {} \n".format(total_quantity))
print("Средняя цена товара: {} \n".format(average_price))
print("Самые дорогие товары: {} \n".format(max_cost_goods))
print("Самые дешевые товары: {} \n".format(min_cost_goods))
print("Заканчивается товар: {} \n".format(min_quantity_goods))
