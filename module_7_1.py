class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        all_products = file.read()
        file.close()
        return all_products

    def add(self, *products):
        all_products = self.get_products()
        file = open(self.__file_name, 'a')
        for i in products:
            if i.name in all_products:
                print(f'Продукт  {i.name} уже есть в магазине')
            else:
                file.write(f'\n{i}')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
