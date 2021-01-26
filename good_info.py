from datetime import date, datetime, timedelta
import logging


class GoodInfo:
    """
    Представляет собой класс, представляющий товар
    Свойства:
        name - название товара
        quantity - количество
        price - цена
        delivery_date - дата поставки
        production_date - дата производства
        shelf_life - срок годности
    Методы:
        __init__(self, str, int, int, date, date, int)
        __str__(self)
        __getitem__(self, str)
        convert_to_date(str)
        data_validation(str, int, int, str, str, int)
    """

    name = None
    count = None
    price = None
    delivery_date = None
    production_date = None
    shelf_life = None

    def __init__(self,
                 name,
                 price,
                 count,
                 delivery_date,
                 production_date,
                 shelf_life):
        """
        Пользователь не должен иметь доступ к инициализации
        Формат при инициализации не проверяется
        Добавлять следует через GoodInfoList.add

        Формат свойств:
        name: str, уникальный вместе с production_date
        price: int > 0
        count: int >= 0
        delivery_date: date, меньше либо равна текущей дате
        production_date: date, <= delivery_date
        shelf_life: int > 0
        """

        self.name = name
        self.count = count
        self.price = price
        self.delivery_date = delivery_date
        self.production_date = production_date
        self.shelf_life = shelf_life

    def __str__(self):
        return '{}: {}руб, {}шт, {}, произеден: {} годен: {}дн'.format(
            self.name,
            self.price,
            self.count,
            self.delivery_date.strftime('%d/%m/%Y'),
            self.production_date.strftime('%d/%m/%Y'),
            self.shelf_life)

    def __getitem__(self, key):
        """
        Получает элемент из GoodInfo по индексу
        :param key: str
        :return: GoodInfo.key
        """

        logger = logging.getLogger("loggerApp.GoodInfo.__getitem__")

        if key == 0 or key == 'name':
            return self.name
        elif key == 1 or key == 'price':
            return self.price
        elif key == 2 or key == 'count':
            return self.count
        elif key == 3 or key == 'delivery_date':
            return self.delivery_date
        elif key == 4 or key == 'production_date':
            return self.production_date
        elif key == 5 or key == 'shelf_life':
            return self.shelf_life
        else:
            logger.error('Такого ключа не существует: {}'.format(key))
            print('Такого ключа не существует: {}'.format(key))

    @staticmethod
    def __convert_to_date(date_str):
        """
        Конвертирует строку формата YYYY-MM-DD в дату
        :param date_str: str
        :return: date (or bool if wrong date)
        """

        logger = logging.getLogger("loggerApp.GoodInfo.__convert_to_date")

        if isinstance(date_str, date):
            return date_str

        date_str = date_str.split('-')
        if date_str[0].isdigit() and \
                date_str[1].isdigit() and \
                date_str[2].isdigit():

            try:
                valid_date = date(day=int(date_str[2]),
                                  month=int(date_str[1]),
                                  year=int(date_str[0]))
            except ValueError:
                print('Неверный формат даты: {}'.format(date_str))
                logger.error('Неверный формат даты: {}'.format(date_str))
                return False

            return valid_date
        else:
            print('Неверный формат даты: {}'.format(date_str))
            logger.error('Неверный формат даты: {}'.format(date_str))
            return False

    @staticmethod
    def data_validation(name, price, count, delivery_date, production_date,
                        shelf_life):
        """
        Проверяет входные параметры, и если они корректные,
        формирует класс GoodInfo; возвращает false в ином случае
        :param name: str
        :param price: int
        :param count: int
        :param delivery_date: str 'YYYY-MM-DD'
        :param production_date: str 'YYYY-MM-DD'
        :param shelf_life: int
        :return: GoodInfo or bool
        """

        price = str(price)
        count = str(count)
        shelf_life = str(shelf_life)

        if not name:
            return False

        if (not price.isdigit() and not count.isdigit() and
                not shelf_life.isdigit()):
            return False

        price = int(price)
        count = int(count)
        shelf_life = int(shelf_life)
        delivery_date = GoodInfo.__convert_to_date(delivery_date)
        production_date = GoodInfo.__convert_to_date(production_date)

        if (shelf_life > 0 and price > 0 and count >= 0
                and delivery_date and production_date
                and datetime.now().date() >= delivery_date >= production_date):

            return GoodInfo(name, price, count, delivery_date, production_date,
                            shelf_life)
        else:
            return False


class GoodInfoList:
    """
    Представляет собой класс - список товаров,
    содержащий методы работы с товарами и их учетом
        good_info_list: str
    Методы:
        __init__(self)
        __str__(self)
        __getitem__(self, str)
        __if_exists(list, str, date)
        read_from_file(self, list)
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
                logger.error('Такого ключа не существует: {}'.format(key))
                print('Такого ключа не существует: {}'.format(key))
            else:
                return self.good_info_list[key]

        # ВЫДАЧА ПО КЛЮЧУ ПРОВЕРИТЬ! и в описание добавить
        elif isinstance(key, str):
            for good in self.good_info_list:
                if good[0] == key:
                    return good

    def __len__(self):
        return len(self.good_info_list)

    @staticmethod
    def __if_exists(good_info_list, name, production_date):
        """
        Проверяет на наличие товара с таким названием и датой производства
            в указанном списке
        :param good_info_list: list
        :param name: str
        :param production_date: date
        :return: bool
        """

        logger = logging.getLogger("loggerApp.GoodInfoList.__if_exists")

        if any(map(lambda good_info:
                   (good_info[0] == name and good_info[4] == production_date),
                   good_info_list)):
            logger.error('Такой товар уже есть: {}, {}'
                         .format(name, production_date))
            print('Такой товар уже есть: {}, {}'.format(name, production_date))
            return True
        else:
            return False

    def read_from_file(self, data_list):
        """
        Создает GoodInfoList из писка товаров формата str:int:int:str:str:int
        :param data_list: list
        """

        logger = logging.getLogger("loggerApp.GoodInfoList.read_from_file")

        for entry in data_list:
            entry.replace('\n', '')
            items = entry.split(":")

            if len(items) != 6:
                print('Не удалось добавить {}'.format(entry))
                logger.error('Не удалось добавить {}'.format(entry))
                continue

            if GoodInfoList.__if_exists(self.good_info_list,
                                        items[0], items[4]):
                print('Не удалось добавить {}'.format(entry))
                logger.error('Не удалось добавить {}'.format(entry))
            else:
                validated_good = GoodInfo.data_validation(items[0],
                                                          items[1],
                                                          items[2],
                                                          items[3],
                                                          items[4],
                                                          items[5])

                if validated_good:
                    self.good_info_list.append(validated_good)
                    # logger.info('Добавлено: {}'.format(validated_good))
                else:
                    print('Не удалось добавить {}'.format(entry))
                    logger.error('Не удалось добавить {}'.format(entry))

    def add(self, other):
        """
        Добавляет элемент класса GoodInfo в список self.good_info_list
        :param other: class GoodInfo
        """

        logger = logging.getLogger("loggerApp.GoodInfoList.add")

        if isinstance(other, GoodInfo):

            if GoodInfoList.__if_exists(self.good_info_list,
                                        other[0], other[4]):

                print('Не удалось добавить {}'.format(other))
                logger.error('Не удалось добавить {}'.format(other))

            else:

                validated_good = GoodInfo.data_validation(other[0],
                                                          other[1],
                                                          other[2],
                                                          other[3],
                                                          other[4],
                                                          other[5])

                if validated_good:
                    logger.info('Добавлено: {}'.format(other))
                    self.good_info_list.append(validated_good)

        else:
            logger.error('class GoodInfo - ошибка добавления')
            print('class GoodInfo - ошибка добавления')

    def remove(self, name):
        """
        Удаляет из GoodInfoList объекты GoodInfo с указанныи именем
            и возвращает их список
        :param name: str
        :return: list
        """

        logger = logging.getLogger("loggerApp.GoodInfoList.remove")

        removed = []
        updated = []

        for good_info in self.good_info_list:
            if good_info.name == name:
                removed.append(good_info)
                logger.info('Удалено: {}'.format(good_info))
            else:
                updated.append(good_info)

            self.good_info_list = updated

        return removed

    def remove_last(self):
        """
        Удаляет из GoodInfoList последний объект GoodInfo и возвращает его
        :return: class GoodInfo
        """

        logger = logging.getLogger("loggerApp.GoodInfoList.remove_last")

        if len(self.good_info_list) > 0:
            last = self.good_info_list[-1]
            del self.good_info_list[-1]
            logger.info('Удалено: {}'.format(last))
            return last

    def remove_expensive(self):
        """
        При помощи метода .get_max_cost находит максимальную цену товара
        и удаляет из GoodInfoList все GoodInfo с такой ценой
        :return: GoodInfoList
        """

        logger = logging.getLogger("loggerApp.GoodInfoList.remove_expensive")

        max_cost = self.get_max_cost().good_info_list[0].price

        removed = GoodInfoList()
        updated_list = []

        for good_info in self.good_info_list:

            if good_info.price == int(max_cost):
                removed.add(good_info)
            else:
                updated_list.append(good_info)

        self.good_info_list = updated_list
        logger.info('Удалены самые дорогие: {}'.format(removed))
        return removed

    def delete_expired(self):
        """
        Удалает все просроченные товары и возвращает их
        :return: class GoodInfoList
        """

        logger = logging.getLogger("loggerApp.GoodInfoList.delete_expired")

        expired_list = GoodInfoList()
        updated_list = []

        for good in self.good_info_list:

            if good[4] + timedelta(days=good[5]) < datetime.now().date():
                expired_list.add(good)
            else:
                updated_list.append(good)

        self.good_info_list = updated_list
        logger.info('Удалены с истекшим сроком годности: {}'
                    .format(expired_list))
        return expired_list

    # remove max cost декоратор?????????????????????????????????????
    def get_max_cost(self):
        """
        Возвращает список товаров с макс стоимостью
        :return: GoodInfoList
        """

        logger = logging.getLogger("loggerApp.GoodInfoList.get_max_cost")

        max_cost = 0
        max_cost_list = GoodInfoList()

        for good_info in self.good_info_list:
            if good_info.price > max_cost:
                max_cost = good_info.price

        for good_info in self.good_info_list:
            if good_info.price == max_cost:
                max_cost_list.add(good_info)

        logger.info('{}'.format(max_cost_list))
        return max_cost_list

    def get_min_cost(self):
        """
        Возвращает список товаров с мин стоимостью
        :return: GoodInfoList
        """

        logger = logging.getLogger("loggerApp.GoodInfoList.get_min_cost")

        min_cost = 999999
        min_cost_list = GoodInfoList()

        for good_info in self.good_info_list:
            if good_info.price < min_cost:
                min_cost = good_info.price

        for good_info in self.good_info_list:
            if good_info.price == min_cost:
                min_cost_list.add(good_info)

        logger.info('{}'.format(min_cost_list))
        return min_cost_list

    def get_min_quantity(self):
        """
        Возвращает список товаров с мин количеством
        :return: GoodInfoList
        """

        logger = logging.getLogger("loggerApp.GoodInfoList.get_min_quantity")

        min_quantity = 999999
        min_quantity_list = GoodInfoList()

        for good_info in self.good_info_list:
            if good_info.count < min_quantity:
                min_quantity = good_info.count

        for good_info in self.good_info_list:
            if good_info.count == min_quantity:
                min_quantity_list.add(good_info)

        logger.info('{}'.format(min_quantity_list))
        return min_quantity_list

    def __bubble_sort(self, param=0):
        """
        Принимает индексы объектов GoodInfo[0-5]
        и сортирует их в GoodInfoList
        :param param: int, str, date
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
        elif key == 'shelf_life':
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
        logger.info('{}'.format(count))
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
            avg = count / len(self.good_info_list)
            logger.info('{}'.format(avg))
            return avg
        else:
            logger.info('{}'.format(0))
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
            std = (summ / len(self.good_info_list)) ** .5
            logger.info('{}'.format(std))
            return std
        else:
            logger.info('{}'.format(0))
            return 0
