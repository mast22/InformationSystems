class BussinessStep:
    step = 0

    def next_step(self):
        self.step += 1


class Bussiness:
    value = 30000


class Order:

    def __init__(self, material_required):
        self.material_required = material_required
