import logging
import logging.config
from logs_processor import LogsProcessor
from good_info import GoodInfoList
from file_processor import FileProcessor

PROGRAM_MODE = 'test'


def main():
    logs_processor = LogsProcessor()
    logs_processor.select_logs_path(PROGRAM_MODE)
    logging.config.dictConfig(logs_processor.get_dict_config())

    # logger = logging.getLogger("loggerApp")
    # logger.info("Program started")

    goods_list = GoodInfoList()
    file_goods = FileProcessor()
    file_data = file_goods.select_path(PROGRAM_MODE)
    goods_list.read_from_file(file_data)
    # file_goods.save_file()

    # ТЕСТ _______________________________________________________________
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
    print('К-во товаров: ', len(goods_list))
    print('Отклонение: ', goods_list.get_std())
    print(goods_list.remove_last())
    print(goods_list['Товар 1'])
    print('Просрочено: ', goods_list.delete_expired())
    print('Самые дорогие удалены: ', goods_list.remove_expensive())


if __name__ == "__main__":
    main()
