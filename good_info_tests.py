from good_info import GoodInfoList, GoodInfo
from file_processor import FileProcessor
import unittest


def get_test_list(test_path='test_data/test0.info'):
    goods_list = GoodInfoList()
    file_goods = FileProcessor()
    file_data = file_goods.select_path(mode='test', path=test_path)
    goods_list.read_from_file(file_data)
    return goods_list


test_path0 = 'test_data/test0.info'
test_path1 = 'test_data/test1.info'
test_path2 = 'test_data/test2.info'
test_path3 = 'test_data/test3.info'
test_path4 = 'test_data/test4.info'
test_path5 = 'test_data/test5.info'
test_path6 = 'test_data/test6.info'


# 0 - пустой список
# 1 - верный список
# 2 - список с неверными значениями
# 3 - список с одинаковыми товарами
# 4 - список для сортировки
# 5 - список для удаления товаров
# 6 - список для продажи товаров

class GoodInfoTest(unittest.TestCase):

    # - тест на проверку общего количества товаров
    def test_total_quantity(self):
        quantity0 = get_test_list(test_path0).get_quantity()
        quantity1 = get_test_list(test_path1).get_quantity()

        self.assertEqual(
            (quantity0, quantity1), (0, 9991)
        )

    # - тест на проверку количества разных видов товаров
    def test_different_quantity(self):
        quantity3 = get_test_list(test_path3).get_quantity()

        self.assertEqual(
            quantity3, 202
        )

    # - тест на проверку средней цены товаров
    def test_get_average(self):
        avg0 = get_test_list(test_path0).get_average_price()
        avg1 = get_test_list(test_path1).get_average_price()

        self.assertEqual(
            (avg0, avg1), (0, 100.1)
        )

    # - тест на проверку отклонения цен товаров
    def test_get_std(self):
        get_std0 = get_test_list(test_path0).get_std()
        get_std1 = get_test_list(test_path1).get_std()

        self.assertEqual(
            (round(get_std0, 1), round(get_std1, 1)), (0, 0.5)
        )

    # - тест на проверку самых дорогих товаров
    def test_get_max_cost(self):
        max_cost0 = str(get_test_list(test_path0)
                        .get_max_cost()).replace('\n', '')
        max_cost1 = str(get_test_list(test_path1)
                        .get_max_cost()).replace('\n', '')

        self.assertEqual(
            (max_cost0, max_cost1),
            ('', 'Товар 2: 101руб, 999шт, 2021-01-02, произеден: 2021-01-01 '
                 'годен: 100днТовар 3: 101руб, 998шт, 2021-01-02, произеден: '
                 '2021-01-01 годен: 100дн')
        )

    # - тест на проверку заканчивающихся товаров
    def test_min_quantity(self):
        min_quantity0 = str(
            get_test_list(test_path0).get_min_quantity()).replace('\n', '')
        min_quantity1 = str(
            get_test_list(test_path1).get_min_quantity()).replace('\n', '')

        self.assertEqual(
            (min_quantity0, min_quantity1),
            ('', 'Товар 5: 100руб, 996шт, 2021-01-02, произеден: 2021-01-01 '
                 'годен: 100дн')
        )

    # - тест на сортировку
    def test_sort(self):
        goods_list0 = get_test_list(test_path0)
        goods_list4 = get_test_list(test_path4)
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
    def test_add_wrong_name(self):
        goods_list0 = get_test_list(test_path0)
        goods_list0.add(GoodInfo(name='',
                                 count=1000,
                                 price=99,
                                 delivery_date='2021-01-10',
                                 production_date='2021-01-01',
                                 shelf_life=100))
        self.assertEqual(str(goods_list0).replace('\n', ''), '')

    # - тест на добавление товаров с неправильным сроком годности
    def test_add_wrong_date(self):
        goods_list0 = get_test_list(test_path0)
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

        self.assertEqual(str(goods_list0).replace('\n', ''), '')

    # - тест на добавление товара с отрицательной ценой
    def test_add_wrong_price(self):
        goods_list0 = get_test_list(test_path0)
        goods_list0.add(GoodInfo(name='Товар 1',
                                 count=1000,
                                 price=-99,
                                 delivery_date='2021-01-10',
                                 production_date='2021-01-01',
                                 shelf_life=100))

        self.assertEqual(str(goods_list0).replace('\n', ''), '')

    # - тест на добавление товара с отрицательным, либо нулевым количеством
    def test_add_wrong_count(self):
        goods_list0 = get_test_list(test_path0)
        goods_list0.add(GoodInfo(name='Товар 1',
                                 count=0,
                                 price=99,
                                 delivery_date='2021-01-10',
                                 production_date='2021-01-01',
                                 shelf_life=100))

        self.assertEqual(str(goods_list0).replace('\n', ''), '')

    # - тест на добавление товаров с истёкшим сроком годности
    def test_add_expired(self):
        goods_list0 = get_test_list(test_path0)
        goods_list0.add(GoodInfo(name='Товар 1',
                                 count=0,
                                 price=99,
                                 delivery_date='2020-01-10',
                                 production_date='2020-01-01',
                                 shelf_life=1))

        self.assertEqual(str(goods_list0).replace('\n', ''), '')

    # - тест на считывание списка товаров из файла
    def test_read_file(self):
        goods_list2 = get_test_list(test_path2)
        self.assertEqual(str(goods_list2).replace('\n', ''), '')

    # - тест на считывание пустых строк из файла в список товаров
    def test_read_file_empty(self):
        goods_list2 = get_test_list(test_path2)
        self.assertEqual(str(goods_list2).replace('\n', ''), '')

    # - тест на считывание строк ":::" из файла в список товаров
    def test_read_file_nofields(self):
        goods_list2 = get_test_list(test_path2)
        self.assertEqual(str(goods_list2).replace('\n', ''), '')

    # - тест на удаление товара
    def test_remove(self):
        goods_list5 = get_test_list(test_path5)
        goods_list5.remove('Товар 1')
        self.assertEqual(str(goods_list5).replace('\n', ''),
                         'Товар 5: 9999руб, 996шт, 2021-01-02, произеден: '
                         '2021-01-01 годен: 100днТовар 6: 9999руб, 1001шт, '
                         '2021-01-02, произеден: 2021-01-01 годен: 100дн')

    # - тест на удаление дорогого товара
    def test_remove_expensive(self):
        goods_list5 = get_test_list(test_path5)
        goods_list5.remove_expensive()
        self.assertEqual(str(goods_list5).replace('\n', ''),
                         'Товар 1: 100руб, 1000шт, 2021-01-02, произеден: '
                         '2021-01-01 годен: 100дн')

    # - тест на продажу 1 товара
    def test_purchase_one(self):
        goods_list6 = get_test_list(test_path6)
        purchase6 = goods_list6.purchase('Товар 1', 5)

        self.assertEqual(
            purchase6, 500
        )

    # - тест на продажу количества товаров больших чем есть
    def test_purchase_many(self):
        goods_list6 = get_test_list(test_path6)
        purchase6 = goods_list6.purchase('Товар 2', 9999)

        self.assertEqual(
            purchase6, None
        )

    # - тест на продажу несуществующих товаров
    def test_purchase_unexisted(self):
        goods_list6 = get_test_list(test_path6)
        purchase6 = goods_list6.purchase('Товар 99', 1)

        self.assertEqual(
            purchase6, None
        )

    # - тест на продажу отсутствующих товаров
    def test_purchase_absent(self):
        goods_list6 = get_test_list(test_path6)
        purchase6 = goods_list6.purchase('Товар 10', 1)

        self.assertEqual(
            purchase6, None
        )


if __name__ == '__main__':
    unittest.main()
