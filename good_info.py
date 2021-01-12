from datetime import date, datetime, timedelta
import logging

module_logger = logging.getLogger("loggerApp.GoodInfoList")


class GoodInfo:
    """
    Представляет собой класс в котором находятся свойства:
        name: str - название товара
        quantity: int - количество
        price: int - цена
        delivery_date: string yyyy-mm-dd - дата поставки
        expiration_date: int - срок годности
    Методы:
        __init__(self, str, int, int, date, int)
        __str__(self)
        __getitem__(self, str)
        convert_to_date(str)
    """
    name = None
    quantity = None
    price = None
    delivery_date = None
    expiration_date = None

    def __init__(self, name, price, quantity, delivery_date, expiration_date):
        """
        :param name: str
        :param price: int
        :param quantity: int
        :param delivery_date: date
        :param expiration_date: int
        """
        self.name = name
        self.quantity = quantity
        self.price = price
        self.delivery_date = self.convert_to_date(delivery_date)
        self.expiration_date = expiration_date

    def __str__(self):
        return '{}: {}руб, {}шт, {}, годен: {}дн'.format(self.name,
                                                         self.price,
                                                         self.quantity,
                                                         self.delivery_date
                                                         .strftime('%d/%m/%Y'),
                                                         self.expiration_date)

    def __getitem__(self, key):
        """
        Получает элемент из GoodInfo по индексу
        :param key: str
        :return: class GoodInfo
        """
        logger = logging.getLogger("loggerApp.GoodInfo.__getitem__")

        if key == 0 or key == 'name':
            return self.name
        elif key == 1 or key == 'price':
            return self.price
        elif key == 2 or key == 'count':
            return self.quantity
        elif key == 3 or key == 'delivery_date':
            return self.delivery_date
        elif key == 4 or key == 'expiration_date':
            return self.expiration_date
        else:
            logger.error('key does not exist - {}'.format(key))
            raise IndexError('{}'.format(key))

    @staticmethod
    def convert_to_date(date_str):
        """
        Коныертирует строку в дату
        :param date_str: str
        :return: date (or bool if wrong type)
        """
        logger = logging.getLogger("loggerApp.GoodInfo.convert_to_date")

        date_str = date_str.split('-')
        if date_str[0].isdigit() and \
                date_str[1].isdigit() and \
                date_str[2].isdigit():
            return date(day=int(date_str[2]),
                        month=int(date_str[1]),
                        year=int(date_str[0]))
        else:
            print('НЕВЕРНАЯ ДАТА')
            logger.error('wrong date - {}'.format(date_str))
            return False


class GoodInfoList:
    """
    Представляет собой класс - список товаров, содержащий методы
    работы с ними
    good_info_list: str
    Методы:
        __init__(self)
        __str__(self)
        __getitem__(self, str)
        read_from_file(self, str)
        add(self, class GoodInfo)
        remove(self, str)
        remove_last(self)
        remove_expensive(self)
        delete_expired(self)
        get_max_cost(self)
        get_min_cost(self)
        get_min_quantity(self)
        __bubble_sort(self, param=0: int)
        sort(self, str)
        get_quantity(self)
        get_average_price(self)
        get_std(self)
        """
    good_info_list = None

    def __init__(self):
        self.good_info_list = []

    def __str__(self):
        result = []
        for good in self.good_info_list:
            result.append(str(good))
        return '\n' + '\n'.join(result) + '\n'

    def __getitem__(self, key):
        """
        Получает элемент из списка GoodInfoList по индексу
        :param key: str
        :return: class GoodInfo or None
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.__getitem__")

        if isinstance(key, int):
            if key >= len(self.good_info_list):
                logger.error('key does not exist - {}'.format(key))
                raise IndexError('{}'.format(key))
            else:
                return self.good_info_list[key]

        elif isinstance(key, str):
            for good in self.good_info_list:
                if good[0] == key:
                    return good

    def __len__(self):
        return len(self.good_info_list)

    @staticmethod
    def __is_valid(items):
        """
        Проверка на правильность представления данных в списке
        :param items: list
        :return: boolean
        """
        if len(items) == 5 and items[1].isdigit() \
                and items[2].isdigit() \
                and GoodInfo.convert_to_date(items[3]) \
                and items[4].replace("\n", "").isdigit() \
                and int(items[4].replace("\n", "")) > 0 \
                and GoodInfo \
                .convert_to_date(items[3]) >= datetime.now().date():
            return True
        else:
            return False

    def read_from_file(self, file):
        """
        Создает GoodInfoList из файла записей формата str:int:int:str:int,
        :param file: str
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.read_from_file")

        with open(file, 'r', encoding="utf-8") as data_file:
            data = data_file.readlines()

        for entry in data:
            items = entry.split(":")

            if any(map(lambda good_info:
                       good_info[0] == items[0], self.good_info_list)):
                logger.error('already exists {}'.format(items))
                print("Такой товар уже есть! {}".format(items))
            else:

                if self.__is_valid(items):

                    self.add(GoodInfo(items[0],
                                      int(items[1]),
                                      int(items[2]),
                                      items[3],
                                      int(items[4].replace("\n", ""))))

                    logger.info('added {}'.format(items))

                else:
                    print('неверный формат {}'.format(items))
                    logger.error('wrong format {}'.format(items))

    @staticmethod
    def __is_goodinfo_valid(good):
        """
        Проверка на правильность данных в GoodInfo
        :param good: GoodInfo
        :return: boolean
        """
        if int(good[4]) > 0 and good[3] >= datetime.now().date():
            return True
        else:
            return False

    def add(self, other):
        """
        Добавляет элемент класса GoodInfo в список, если такого товара еще нет
        :param other: class GoodInfo
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.add")

        if isinstance(other, GoodInfo):
            if any(map(lambda good_info:
                       good_info[0] == other[0], self.good_info_list)):
                logger.error('already exists {}'.format(other))
                print("Такой товар уже есть!")
            else:
                if self.__is_goodinfo_valid(other):
                    # logger.info('added {}'.format(other))
                    self.good_info_list.append(other)
                else:
                    logger.error('cant add {}'.format(other))
                    print('неверный формат {}'.format(other))
        else:
            logger.error('cant add {}'.format(other))
            raise ValueError('{}'.format(other))

    def remove(self, name):
        """
        Удаляет из GoodInfoList объект GoodInfo с указанныи именем
        :param name: str
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.remove")

        for good_info in self.good_info_list:
            if good_info.name == name:
                logger.info('removed {}'.format(good_info))
                self.good_info_list.remove(good_info)

    def remove_last(self):
        """
        Удаляет из GoodInfoList последний объект GoodInfo и возвращает его
        :return: class GoodInfo
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.remove_last")

        if len(self.good_info_list) > 0:
            last = self.good_info_list[-1]
            del self.good_info_list[-1]
            logger.info('removed {}'.format(last))
            return last

    def remove_expensive(self):
        """
        При помощи метода .get_max_cost находит максимальную цену товара
        и удаляет из GoodInfoList все GoodInfo с такой ценой
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.remove_expensive")

        max_cost = self.get_max_cost().split(':')[1].split(',')[0] \
            .replace("руб", "").replace(" ", "")

        for good_info in self.good_info_list:
            if good_info.price == int(max_cost):
                logger.info('removed {}'.format(good_info))
                self.good_info_list.remove(good_info)

    def delete_expired(self):
        """
        Удалает все просроченные товары и возвращает их
        :return: class GoodInfoList
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.delete_expired")

        expired_list = GoodInfoList()
        for good in self.good_info_list:
            if good[3] + timedelta(days=good[4]) < datetime.now().date():
                expired_list.add(good)
                self.remove(good[0])
        logger.info('expired removed {}'.format(expired_list))
        return expired_list

    def get_max_cost(self):
        """
        Возвращает список товаров с макс стоимостью
        :return: list of GoodInfo
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.get_max_cost")
        max_cost = 0
        max_cost_list = []

        for good_info in self.good_info_list:
            if good_info.price > max_cost:
                max_cost = good_info.price

        for good_info in self.good_info_list:
            if good_info.price == max_cost:
                max_cost_list.append(str(good_info))

        logger.info("get_max_cost DONE")
        return '\n' + '\n'.join(max_cost_list)

    def get_min_cost(self):
        """
        Возвращает список товаров с мин стоимостью
        :return: list of GoodInfo
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.get_min_cost")

        min_cost = 99999
        min_cost_list = []

        for good_info in self.good_info_list:
            if good_info.price < min_cost:
                min_cost = good_info.price

        for good_info in self.good_info_list:
            if good_info.price == min_cost:
                min_cost_list.append(str(good_info))

        logger.info("get_min_cost DONE")
        return '\n' + '\n'.join(min_cost_list)

    def get_min_quantity(self):
        """
        Возвращает список товаров с мин количеством
        :return: list of GoodInfo
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.get_min_quantity")

        min_quantity = 99999
        min_quantity_list = []

        for good_info in self.good_info_list:
            if good_info.quantity < min_quantity:
                min_quantity = good_info.quantity

        for good_info in self.good_info_list:
            if good_info.quantity == min_quantity:
                min_quantity_list.append(str(good_info))

        logger.info("get_min_quantity DONE")
        return '\n' + '\n'.join(min_quantity_list)

    def __bubble_sort(self, param=0):
        """
        Принимает индексы объектов GoodInfo[0-4]
        и сортирует их в GoodInfoList
        :param param: int, str
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
        Принимает на вход строку key = 'name', 'count', 'cost',
        'delivery_date', 'expiration_date' и применяет
        функцию сортировки по указанному значению
        :param key: str
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.sort")

        if key == 'name':
            self.__bubble_sort(0)
            logger.info("sorted by name")
        elif key == 'count':
            self.__bubble_sort(2)
            logger.info("sorted by count")
        elif key == 'cost':
            self.__bubble_sort(1)
            logger.info("sorted by cost")
        elif key == '':
            self.__bubble_sort(3)
            logger.info("sorted by delivery date")
        elif key == 'expiration_date':
            self.__bubble_sort(4)
            logger.info("sorted by expiration date")
        else:
            logger.error("wrong sorting key {}".format(key))
            print('Невозможно отсортировать по значению {}'.format(key))

    def get_quantity(self):
        """
        Получает общее количество всех товаров
        :return: int
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.get_quantity")

        count = 0
        for good in self.good_info_list:
            count += good[2]
        logger.info("get_quantity DONE")
        return count

    def get_average_price(self):
        """
        Получает среднюю цену по всем товарам
        :return: float
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.get_average_price")

        count = 0
        for good in self.good_info_list:
            count += good[1]
        if len(self.good_info_list) > 0:
            logger.info("get_average_price DONE")
            return count / len(self.good_info_list)
        else:
            logger.info("get_average_price DONE")
            return 0

    def get_std(self):
        """
        Получает среднее отклонение для всех цен товаров
        :return: float
        """
        logger = logging.getLogger("loggerApp.GoodInfoList.get_std")

        average = self.get_average_price()
        summ = 0
        for good in self.good_info_list:
            summ += (good.price - average) ** 2
        if len(self.good_info_list) > 0:
            logger.info("get_std DONE")
            return (summ / len(self.good_info_list)) ** .5
        else:
            logger.info("get_std DONE")
            return 0
