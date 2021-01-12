import logging
import logging.config
import os
import pathlib

from good_info import GoodInfoList, GoodInfo


def create_logs_path(logs_path):
    """
    Создает директорию с файлом logs.log по заданному пути
    :param logs_path: string
    """
    logger = logging.getLogger("loggerApp.GoodInfoList.read_from_file")

    if os.path.exists(os.path.join(logs_path, 'logs.log')):
        print("Указанный файл существует")
        logger.error('file already exists {}'.format(logs_path))
    else:
        pathlib.Path(logs_path).mkdir(parents=True, exist_ok=True)
        open(os.path.join(logs_path, 'logs.log'), 'tw',
             encoding='utf-8').close()
        logger.info('file created {}'
                    .format(os.path.join(logs_path, 'logs.log')))


def check_data_path(data_path):
    """
    Проверяет на наличие пути к файлу, если нет - задает по умолчанию
    :param data_path: string
    :return: string
    """
    if os.path.exists(data_path):
        print("Указанный файл существует")
        return data_path
    else:
        print("Файл не существует")
        return 'data/goods2.info'


def main():
    # Пути к файлу и логам
    DATA_PATH = check_data_path('data/goods2.info')
    LOGS_PATH = '../ListOfGoods/logs'

    # ЛОГГЕР
    create_logs_path(LOGS_PATH)

    dictLogConfig = {
        "version": 1,
        "handlers": {
            "fileHandler": {
                "class": "logging.FileHandler",
                "formatter": "myFormatter",
                "filename": os.path.join(LOGS_PATH, 'logs.log'),
                "encoding": "utf-8"
            }
        },
        "loggers": {
            "loggerApp": {
                "handlers": ["fileHandler"],
                "level": "INFO",
            }
        },
        "formatters": {
            "myFormatter": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
    }

    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger("loggerApp")

    # РАБОТА С ФАЙЛОМ
    logger.info("Program started")
    goods_list = GoodInfoList()
    goods_list.read_from_file(DATA_PATH)

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

    print(goods_list)
    # __len__() для GoodInfolist
    print(len(goods_list))
    # get_std() получает среднее отклонение для всех цен товаров
    print(goods_list.get_std())
    # remove_last() удаляет последний товар
    print(goods_list.remove_last())

    print(goods_list)

    print(goods_list['соль 1 кг'])

    # Проверка на правильность ввода через add
    a = GoodInfo('Товар1', 50, 30, '2021-12-30', 720)
    b = GoodInfo('пшено 1кг', 50, 30, '2021-12-30', 720)
    c = GoodInfo('Товар2', 50, 30, '2019-12-30', 720)
    d = GoodInfo('Товар3', 50, 30, '2021-12-30', -720)
    goods_list.add(a)
    goods_list.add(b)
    goods_list.add(c)
    goods_list.add(d)

    print(goods_list)


if __name__ == "__main__":
    main()
