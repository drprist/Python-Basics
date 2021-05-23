key_name = "Название"
key_price = "Цена"
key_lot = "Количество"
key_unit = "Единица"

list_1 = list()
list_names = list()
list_prices = list()
list_lots = list()
list_units = list()

user_agree = 'Y'
i = 1
while user_agree == 'Y':
    user_name = input("Введите название товара: ")
    user_price = input("Введите цену товара: ")
    user_lot = input("Введите количество товара: ")
    user_unit = input("Введите единицу измерения товара: ")
    dict_1 = {
        key_name: user_name,
        key_price: int(user_price),
        key_lot: int(user_lot),
        key_unit: user_unit
    }
    tuple_1 = (i, dict_1)
    i += i
    list.append(list_1, tuple_1)
    list.append(list_names, user_name)
    list.append(list_prices, user_price)
    list.append(list_lots, user_lot)
    list.append(list_units, user_unit)
    user_agree = input("Для продолжения ввода товаров введите 'Y'. Для прекращения ввода нажмите 'Enter': ")
    if user_agree != 'Y':
        print("Введенные товары:\n ", list_1)

dict_2 = {
    key_name: list(set(list_names)),
    key_price: list(set(list_prices)),
    key_lot: list(set(list_lots)),
    key_unit: list(set(list_units))
}
print("Аналитика по товарам:\n ", dict_2)
