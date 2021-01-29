# ListOfGoods
Программа, помогающая проводить учет товаров.
Состоит из двух модулей good_info и reporter, запуск производится из reporter

Создает список товаров из готового файла(по умолчанию - data/goods2.info).
Содержит различные методы для работы с данными:

    read_from_file(self, str) - формирует список товаров класса GoodInfoList из файла
    add(self, class GoodInfo) - добавление товара в список
    remove(self, str) - удаление товара из списка
    remove_last(self) - удаление последнего товара в списке
    remove_expensive(self) - удаление товаров с самой высокой ценой
    delete_expired(self) - удаление просроченных товаров из списка
    get_max_cost(self) - получение товара с макс стоимостью
    get_min_cost(self) - получение товара с мин стоимостью
    get_min_quantity(self) - получение товара с мин количеством
    sort(self, str) - сортировка товаров по выбранному значению
    get_quantity(self) - общее количество товаров
    get_average_price(self) - средняя цена товаров
    get_std(self) - среднее отклонение для всех цен товаров
    purchase(self, str, int) - покупка товара
