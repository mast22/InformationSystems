from core import bussiness_objects as bo
from core import bussiness_logic as bl
from core import bussiness_resources as br

from constants import *


def operate(bussiness, material, order):
    if step.step == 0:
        print(start_msg % (bussiness.value, material.price, order.material_required))

        material_bought = int(input())
        bussiness.value -= material_bought * material.price


def complete_day(bussiness, material, order, warehouse, step):
    # В конце дня изготавливается и продаётся продукт
    # Делает отчёт по дню
    warehouse.check_capacity()
    if not warehouse.use_material(order.material_required):
        # Ваш заказ выполнен, вы заработали деньги
        earned = order.material_required * material.price * 1.5
        bussiness.value = earned

        print(f'Вы заработали {earned}')
        print('Введите объём заказа, в количестве материала, который вы хотите взять')
        order = bl.Order(int(input()))
    else:
        bussiness.value -= order.material_required * 0.1
        print('Вы понесли неустойку за невыполненный заказ, вам придется выполнить его ещё раз')

    if bussiness.value < 0:
        print('Вы ушли в ещё больше долги, ваш бизнесс больше не может существовать')
        return None

    print(stat_msg.format(step.step, bussiness.value,
                          order.material_required, material.price))

    step.next_step()


if __name__ == '__main__':
    bussiness = bl.Bussiness()
    step = bl.BussinessStep()

    material = br.Material()

    order = bl.Order(100)

    warehouse = bo.WareHouse()

    while True:
        operate(bussiness, material, order)
        result = complete_day(bussiness, material, order, warehouse, step)
        if not result:
            print('Вы обанкротились')
        else:
            break
