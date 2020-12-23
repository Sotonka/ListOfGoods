from good_info import GoodInfo, GoodInfoList

DATA_PATH = 'data/goods2.info'
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
