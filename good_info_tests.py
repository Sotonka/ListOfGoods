from good_info import GoodInfoList, GoodInfo
from file_processor import FileProcessor
import unittest

goods_list0 = GoodInfoList()
goods_list1 = GoodInfoList()
goods_list2 = GoodInfoList()
goods_list3 = GoodInfoList()
goods_list4 = GoodInfoList()
goods_list5 = GoodInfoList()
goods_list6 = GoodInfoList()

file_goods0 = FileProcessor()
file_goods1 = FileProcessor()
file_goods2 = FileProcessor()
file_goods3 = FileProcessor()
file_goods4 = FileProcessor()
file_goods5 = FileProcessor()
file_goods6 = FileProcessor()

file_data0 = file_goods0.select_path(mode='test', path='test_data/test0.info')
file_data1 = file_goods1.select_path(mode='test', path='test_data/test1.info')
file_data2 = file_goods2.select_path(mode='test', path='test_data/test2.info')
file_data3 = file_goods3.select_path(mode='test', path='test_data/test3.info')
file_data4 = file_goods4.select_path(mode='test', path='test_data/test4.info')
file_data5 = file_goods5.select_path(mode='test', path='test_data/test5.info')
file_data6 = file_goods6.select_path(mode='test', path='test_data/test6.info')

goods_list0.read_from_file(file_data0)
goods_list1.read_from_file(file_data1)
goods_list2.read_from_file(file_data2)
goods_list3.read_from_file(file_data3)
goods_list4.read_from_file(file_data4)
goods_list5.read_from_file(file_data5)
goods_list6.read_from_file(file_data6)


# 0 - пустой список
# 1 - верный список
# 2 - список с неверными значениями
# 3 - список с одинаковыми товарами
# 4 - список для сортировки
# 5 - список для удаления товаров
# 6 - список для продажи товаров

class GoodInfoTest(unittest.TestCase):

    # - тест на проверку общего количества товаров
    # - тест на проверку количества разных видов товаров
    def test_total_quantity(self):
        quantity0 = goods_list0.get_quantity()
        quantity1 = goods_list1.get_quantity()
        quantity3 = goods_list3.get_quantity()

        self.assertEqual(
            (quantity0, quantity1, quantity3), (0, 9991, 202)
        )

    # - тест на проверку средней цены товаров
    def test_get_average(self):
        avg0 = goods_list0.get_average_price()
        avg1 = goods_list1.get_average_price()

        self.assertEqual(
            (avg0, avg1), (0, 100.1)
        )

    # - тест на проверку отклонения цен товаров
    def test_get_std(self):
        get_std0 = goods_list0.get_std()
        get_std1 = goods_list1.get_std()

        self.assertEqual(
            (round(get_std0, 1), round(get_std1, 1)), (0, 0.5)
        )

    # - тест на проверку самых дорогих товаров
    def test_get_max_cost(self):
        max_cost0 = str(goods_list0.get_max_cost()).replace('\n', '')
        max_cost1 = str(goods_list1.get_max_cost()).replace('\n', '')

        self.assertEqual(
            (max_cost0, max_cost1),
            ('', 'Товар 2: 101руб, 999шт, 2021-01-02, произеден: 2021-01-01 '
                 'годен: 100днТовар 3: 101руб, 998шт, 2021-01-02, произеден: '
                 '2021-01-01 годен: 100дн')
        )

    # - тест на проверку заканчивающихся товаров
    def test_min_quantity(self):
        min_quantity0 = str(goods_list0.get_min_quantity()).replace('\n', '')
        min_quantity1 = str(goods_list1.get_min_quantity()).replace('\n', '')

        self.assertEqual(
            (min_quantity0, min_quantity1),
            ('', 'Товар 5: 100руб, 996шт, 2021-01-02, произеден: 2021-01-01 '
                 'годен: 100дн')
        )

    # - тест на сортировку
    def test_sort(self):
        goods_list0.sort('name')
        goods_list4.sort('name')
        sorted0 = str(goods_list0).replace('\n', '')
        sorted4 = str(goods_list4).replace('\n', '')

        self.assertEqual(
            (sorted0, sorted4),
            ('',
             'Товар 1: 101руб, 1000шт, 2021-01-04, произеден: 2021-01-02 '
             'годен: 100днТовар 2: 101руб, 999шт, 2021-01-01, произеден: '
             '2021-01-01 годен: 100днТовар 3: 100руб, 998шт, 2021-01-05, '
             'произеден: 2021-01-04 годен: 100днТовар 4: 102руб, 997шт, '
             '2021-01-03, произеден: 2021-01-02 годен: 100днТовар 5: 99руб, '
             '996шт, 2021-01-02, произеден: 2021-01-01 годен: 100дн')
        )

    # - тест на добавление товаров без имени
    # - тест на добавление товаров с неправильным сроком годности
    # - тест на добавление товара с отрицательной ценой
    # - тест на добавление товара с отрицательным, либо нулевым количеством
    def test_add(self):
        goods_list0.add(GoodInfo(name='',
                                 count=1000,
                                 price=99,
                                 delivery_date='2021-01-10',
                                 production_date='2021-01-01',
                                 shelf_life=100))

        goods_list0.add(GoodInfo(name='Товар 1',
                                 count=1000,
                                 price=99,
                                 delivery_date='2021-01-10',
                                 production_date='2020-99-01',
                                 shelf_life=100))

        goods_list0.add(GoodInfo(name='Товар 1',
                                 count=1000,
                                 price=99,
                                 delivery_date='2021-01-10',
                                 production_date='2021-01-11',
                                 shelf_life=100))

        goods_list0.add(GoodInfo(name='Товар 1',
                                 count=1000,
                                 price=-99,
                                 delivery_date='2021-01-10',
                                 production_date='2021-01-01',
                                 shelf_life=100))

        goods_list0.add(GoodInfo(name='Товар 1',
                                 count=0,
                                 price=99,
                                 delivery_date='2021-01-10',
                                 production_date='2021-01-01',
                                 shelf_life=100))

        self.assertEqual(str(goods_list0).replace('\n', ''), '')

    # - тест на считывание списка товаров из файла
    # - тест на считывание пустых строк из файла в список товаров
    # - тест на считывание строк ":::" из файла в список товаров
    def test_read_file(self):
        self.assertEqual(str(goods_list2).replace('\n', ''), '')

    # - тест на удаление товара
    def test_remove(self):
        goods_list5.remove('Товар 1')
        self.assertEqual(str(goods_list5).replace('\n', ''),
                         'Товар 5: 9999руб, 996шт, 2021-01-02, произеден: '
                         '2021-01-01 годен: 100днТовар 6: 9999руб, 1001шт, '
                         '2021-01-02, произеден: 2021-01-01 годен: 100дн')

    # - тест на удаление дорогого товара
    def test_remove_expensive(self):
        goods_list5.remove_expensive()
        self.assertEqual(str(goods_list5).replace('\n', ''), '')

    # - тест на продажу 1 товара
    def test_purchase_one(self):
        purchase6 = goods_list6.purchase('Товар 1', 5)

        self.assertEqual(
            purchase6, 500
        )

    # - тест на продажу количества товаров больших чем есть
    def test_purchase_many(self):
        purchase6 = goods_list6.purchase('Товар 2', 9999)

        self.assertEqual(
            purchase6, None
        )

    # - тест на продажу несуществующих товаров
    def test_purchase_unexisted(self):
        purchase6 = goods_list6.purchase('Товар 99', 1)

        self.assertEqual(
            purchase6, None
        )

    # - тест на продажу отсутствующих товаров
    def test_purchase_absent(self):
        purchase6 = goods_list6.purchase('Товар 10', 1)

        self.assertEqual(
            purchase6, None
        )


if __name__ == '__main__':
    unittest.main()
