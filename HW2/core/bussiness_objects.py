class BussinessBase:
    pass


class Director(BussinessBase):
    pass


class Accountant(BussinessBase):
    pass


class Workshop(BussinessBase):
    pass


class WareHouse(BussinessBase):
    maximum_capacity = 1000
    current_capacity = 0

    def check_capacity(self):
        """
        Непоместившийся материал уничтожается под дождём
        """
        if self.current_capacity > self.maximum_capacity:
            self.current_capacity = self.maximum_capacity

        return self.current_capacity

    def use_material(self, used_amount):
        """
        Отправка материала на создание продукта
        Возвращает None если запрошенно меньше материала чем есть
        Возращает оставшееся количество материала если его хватило
        """
        self.current_capacity = self.current_capacity - used_amount

        if self.current_capacity - used_amount < 0:
            return None
        else:
            self.current_capacity = self.current_capacity - used_amount
            return self.current_capacity


class Provider(BussinessBase):
    pass


class Buyer(BussinessBase):
    pass
