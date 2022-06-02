class NotInListException(Exception):
    pass


class OutOfStockException(Exception):
    pass


class Shop:
    def __init__(self):
        self.prices = {'Хлеб': 60, 'Яйца': 100, 'Сосиски': 300, 'Молоко': 80, 'Пиво': 50}
        self.stock = {'Хлеб': 50, 'Яйца': 50, 'Сосиски': 50, 'Молоко': 50, 'Пиво': 50}

    def count_recipt(self, items):
        recipt_amount = 0
        for item in items:
            if item not in self.prices:
                raise NotInListException
            if self.stock[item] == 0:
                raise OutOfStockException

            recipt_amount += self.prices[item]
            self.stock[item] -= 1
        return recipt_amount

    def print_stock(self):
        print('Остаток на складе:')
        for key, val in self.stock.items():
            print(f'{key} - {val}')
        print()


local_shop = Shop()
local_shop.print_stock()
print(local_shop.count_recipt(['Пиво', 'Пиво', 'Пиво', 'Хлеб', 'Хлеб', 'Яйца', 'Сосиски', 'Сосиски', 'Молоко']))
print()
local_shop.print_stock()
