# Третьяков Роман Викторович
# Факультет Geek University Python-разработки
# Урок 2

# 1. Проверить механизм наследования в Python. Для этого создать два класса.
# Первый — родительский (ItemDiscount), должен содержать статическую информацию
# о товаре: название и цену. Второй — дочерний (ItemDiscountReport), должен содержать
# функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
# Проверить работу программы, создав экземпляр (объект) родительского класса.
#                                                       ^^^^^^^^^^^^^
# Родительского класса? Или дочернего, который унаследует свойства родительского???

# class ItemDiscount:
#      def __init__(self, name, price):
#          self.name = name
#          self.price = price
#
# class ItemDiscountReport(ItemDiscount):
#     def __init__(self, name, price):
#         super().__init__(name, price)
#
#     def get_parent_data(self):
#          return self.name + ' ' + str(self.price)
#
#
# item1 = ItemDiscountReport('Товар1', 10)
# item2 = ItemDiscountReport('Товар2', 20)
#
# print(item1.get_parent_data())
# print(item2.get_parent_data())


# 2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться,
# что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.

# class ItemDiscount:
#     def __init__(self, name, price):
#         self.__name = name
#         self.__price = price
#
#
# class ItemDiscountReport(ItemDiscount):
#     def __init__(self, name, price):
#         super().__init__(name, price)
#
#     def get_parent_data(self):
#         return self.name + ' ' + str(self.price)
#
#
# item1 = ItemDiscountReport('Товар1', 10)
# item2 = ItemDiscountReport('Товар2', 20)
#
# print(item1.get_parent_data())
# print(item2.get_parent_data())


# 3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным
# переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_parent_data(self):
        return self.get_name() + ' ' + str(self.get_price())


item1 = ItemDiscountReport('Товар1', 10)
item2 = ItemDiscountReport('Товар2', 20)

print(item1.get_parent_data())
print(item2.get_parent_data())


# 4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и
# родительский, и дочерний классы получили новое значение цены. Следует проверить это,
# вызвав соответствующий метод родительского класса и функцию дочернего (функция, отвечающая
# за отображение информации о товаре в одной строке).

# class ItemDiscount:
#     def __init__(self, name, price):
#         self.__name = name
#         self.__price = price
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_price(self, price):
#         self.__price = price
#
#     #@property
#     def get_name(self):
#         return self.__name
#
#     #@property
#     def get_price(self):
#         return self.__price
#
# class ItemDiscountReport(ItemDiscount):
#     def get_parent_data(self):
#         return self.get_name() + ' ' + str(self.get_price())
#
#
# item1 = ItemDiscount('Товар1', 10)
# item2 = ItemDiscount('Товар2', 20)
#
# item1.set_price(100)
# item2.set_price(200)
# print(item1.get_price)
# print(item2.get_price)
#
# print(ItemDiscountReport.get_parent_data(item1))
# print(ItemDiscountReport.get_parent_data(item2))
#





# 5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве
# аргумента в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса (метод
# init, в который должна передаваться переменная — скидка), и перегрузку метода str дочернего класса.
# В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
# Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы (вторая
# и третья строка после объявления дочернего класса).

# 6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport
# на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
# которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать
# выполнение каждой из функции тремя способами.
