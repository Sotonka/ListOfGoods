from good_info import GoodInfoList, GoodInfo
import unittest

goods_list0 = GoodInfoList()
goods_list1 = GoodInfoList()
goods_list2 = GoodInfoList()
goods_list3 = GoodInfoList()
goods_list4 = GoodInfoList()
goods_list5 = GoodInfoList()
# пустой файл
goods_list0.read_from_file('data/test0.info')
# без ошибок
goods_list1.read_from_file('data/test1.info')
# повторяющиеся товары
goods_list2.read_from_file('data/test2.info')
goods_list4.read_from_file('data/test4.info')
goods_list5.read_from_file('data/test5.info')


class GoodInfoTest(unittest.TestCase):
    # - тест на проверку общего количества товаров
    # - тест на проверку количества разных видов товаров
    def test_total_quantity(self):
        total_quantity0 = goods_list0.get_quantity()
        total_quantity1 = goods_list1.get_quantity()
        total_quantity2 = goods_list2.get_quantity()

        self.assertEqual(
            (total_quantity0, total_quantity1, total_quantity2),
            (0, 90, 80)
        )

    # - тест на проверку средней цены товаров
    def test_average_price(self):
        average_price0 = goods_list0.get_average_price()
        average_price1 = goods_list1.get_average_price()
        average_price2 = goods_list2.get_average_price()

        self.assertEqual(
            (average_price0, average_price1, average_price2),
            (0, 422.2, 55)
        )

    # - тест на проверку среднеквадратического отклонения цен товаров
    def test_get_std(self):
        get_std0 = goods_list0.get_std()
        get_std1 = goods_list1.get_std()
        get_std2 = goods_list2.get_std()

        self.assertEqual(
            (round(get_std0, 1), round(get_std1, 1), round(get_std2, 1)),
            (0, 472.9, 0)
        )

    # - тест на проверку самых дорогих товаров
    def test_max_cost(self):
        max_cost0 = goods_list0.get_max_cost()
        max_cost1 = goods_list1.get_max_cost()

        self.assertEqual(
            (max_cost0, max_cost1),
            ('\n',
             '\n' +
             'Товар 7: 1001руб, 10шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн' +
             '\n' +
             'Товар 8: 1001руб, 10шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн')
        )

    # - тест на проверку заканчивающихся товаров
    def test_min_quantity(self):
        min_quantity0 = goods_list0.get_min_quantity()
        min_quantity1 = goods_list1.get_min_quantity()

        self.assertEqual(
            (min_quantity0, min_quantity1),
            ('\n',
             '\n' +
             'Товар 4: 10руб, 5шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн' +
             '\n' +
             'Товар 5: 50руб, 5шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн')
        )

    # - тест на сортировку
    def test_sort(self):
        goods_list0.sort()
        goods_list1.sort()
        sorted1 = [str(goods_list1).replace('\n', '')]

        self.assertEqual(
            (sorted1),
            ([
                'Товар 1: 50руб, 10шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн' +
                'Товар 10: 5руб, 10шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн' +
                'Товар 2: 100руб, 10шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн' +
                'Товар 3: 1000руб, 10шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн' +
                'Товар 4: 10руб, 5шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн' +
                'Товар 5: 50руб, 5шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн' +
                'Товар 6: 1000руб, 10шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн' +
                'Товар 7: 1001руб, 10шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн' +
                'Товар 8: 1001руб, 10шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн' +
                'Товар 9: 5руб, 10шт, 30/12/2021, произеден: 30/12/2021 годен: 7дн'])
        )


    # - тест на добавление товаров без имени
    # - тест на добавление товаров с неправильным сроком годности
    # - тест на добавление товаров с истёкшим сроком годности
    # - тест на добавление товара с отрицательной ценой
    # - тест на добавление товара с отрицательным, либо нулевым количеством

    def test_add_item(self):
        item1 = GoodInfo('', 50, 30, '2021-12-30', '2021-12-30', 720)
        item2 = GoodInfo('Товар2', 50, 30, '2021-12-30', '2021-12-30', 720)
        item3 = GoodInfo('Товар3', 50, 30, '2021-12-30', '2019-11-30', 720)
        item4 = GoodInfo('Товар4', -50, 30, '2021-12-30', '2021-12-30', 720)
        item5 = GoodInfo('Товар5', 50, -30, '2021-12-30', '2021-12-30', 720)
        item6 = GoodInfo('Товар6', 50, 0, '2021-12-30', '2021-12-30', 720)
        goods_list3.add(item1)
        goods_list3.add(item2)
        goods_list3.add(item3)
        goods_list3.add(item4)
        goods_list3.add(item5)
        goods_list3.add(item6)

        self.assertEqual(
            (str(goods_list3)),
            ('\nТовар2: 50руб, 30шт, 30/12/2021, произеден: 30/12/2021 годен: 720дн\n')
        )

    # - тест на считывание списка товаров из файла
    # - тест на считывание пустых строк из файла в список товаров
    # - тест на считывание строк ":::" из файла в список товаров
# - тест на удаление товара
# - тест на удаление дорогово товара
# - тест на продажу 1 товара
# - тест на продажу количества товаров больших чем есть
# - тест на продажу несуществующих товаров
# - тест на продажу отсутствующих товаров


if __name__ == '__main__':
    unittest.main()
