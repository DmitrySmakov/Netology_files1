
def get_cook_book(filename):  # filename  = 'cook_book.txt'
    cook_book = {}
    with open(filename, "r" ,encoding="utf-8") as file: # 'cook_book.txt'
         for line in file:
             dish = line.strip()
             cook_book[dish] = []
             count = int(file.readline().strip())
             tmp_lst = []
             for sub_str in range(0, count):
                 s = file.readline().strip()
                 lst = s.split('|')
                 dict = {'ingredient_name':lst[0].strip(), 'quantity': int(lst[1].strip()), 'measure':lst[2].strip()}
                 tmp_lst.append(dict)
             cook_book[dish] = tmp_lst
             file.readline().strip() # прогоняем пустую строку , а если она не одна?
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, filename ):
    cook_book = get_cook_book(filename)
    dic = {}
    for dish in dishes: #  <class 'list' Омлет
        tmp_dish = cook_book[dish]
        for ingr in tmp_dish: # <class 'dict'>  {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
            # print(ingr)
            quantity = 0
            if ingr['ingredient_name'] in dic: #  тоже что dic.keys() : # проверка есть ли ключ в dic
                  quantity =  dic[ingr['ingredient_name']]['quantity']  # как ?
            dic[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': ingr['quantity']*person_count+quantity}
    print(dic)
    return

if __name__ == '__main__':
    get_shop_list_by_dishes( ['Омлет', 'Омлет'], 3 , 'cook_book.txt')
