
# if __name__ == '__main__':

# file1 = open('data.txt')
# data = file1.read()
# print(type(data),"\n")
# print(data)
# file1.close()

# with open('cook_book.txt') as f:
#     data = f.read()
#     print(type(data))
#     print(data)

def get_cook_book(filename):  # filename  = 'cook_book.txt'
    cook_book = {}     # словарь  / список словарей
    with open(filename) as file: # 'cook_book.txt'
         for line in file:
             dish = line.strip()
             # ingredients =[]
             cook_book[dish] = []
             count = int(file.readline().strip())
             tmp_lst = []
             for sub_str in range(0, count):
                 s = file.readline().strip()
                 # s= s.replace(" ", "")
                 # lst = s.split()
                 # s = s.replace("|", "") # split по пробелам будет некорректно если два слова в названии

                 lst = s.split('|')
                 dict = {'ingredient_name':lst[0].strip(), 'quantity': int(lst[1].strip()), 'measure':lst[2].strip()}
                 # dict = {}  # или так
                 # dict['ingredient_name'] = lst[0].strip()
                 # dict['quantity'] = lst[1].strip()
                 # dict['measure'] = lst[2].strip()
                 tmp_lst.append(dict)
                 # for i in lst:
                 #     i = i.strip()   # не сработает делаю правильно но не присвается в самом lst
                     # print(i)
                 # tmp.append(f.readline().strip())
                 # sub_dict = {}
                 # a = sub_str
             cook_book[dish] = tmp_lst
              # print(tmp)
             file.readline().strip() # прогоняем пустую строку , а если она не одна?
    # print(cook_book)
    # for k, v in cook_book.items():
    #     print(k)
    #     print(v)
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, filename ):
    cook_book = get_cook_book(filename)
    dic = {}
    for dish in dishes: #  <class 'list' Омлет
        tmp_dish = cook_book[dish]
        for ingr in tmp_dish: # <class 'dict'>  {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
            # print(ingr)
            quantity = 0
            if ingr['ingredient_name'] in dic.keys(): # проверка есть ли ключ в dic
                # quantity =  dic[ingr['ingredient_name']['quantity']]#  неправильно ?
                quantity =  dic[ingr['ingredient_name']]['quantity']  # как ?
                # tmp_dic = dic[ingr['ingredient_name']]
                # print(tmp_dic)
                # quantity = tmp_dic['quantity']
            dic[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': ingr['quantity']*person_count+quantity}
            # print(dic[ingr['ingredient_name']])
    print(dic)
    return

get_shop_list_by_dishes( ['Омлет', 'Омлет'], 3 , 'cook_book.txt')

input('пауза')

# исключить \n из строки удалением
         # if len(line.strip()) != 0:# is  empty: //  not
        # if not line.strip():

            # print('привет')
        #     str = str + line.strip()
        #  print(line.strip())
           # print(len(line.strip()))

# print(cook_book)

input('пауза')
# Var 1
# with open('cook_book.txt') as f:
# #     print(f)
#      for line in f:
#          print(line.strip())

# var 2
# file1 = open('cook_book.txt', "r")
# while True:
#     # считываем строку
#     line = file1.readline()
#     # прерываем цикл, если строка пустая
#     if not line:
#         break
#     # выводим строку
#     print(line.strip())

# var 3
file1 = open('cook_book.txt', "r")
line = file1.readline()
while line:
   print(line.strip())
   line = file1.readline()


    # while (f.readline() != None):
# while not f.closed and (f.readline() != None):
#       for i in range(1,30):
#         print(f.readline().strip())
        # print(f.readline().strip())
        # print(f.read())
    # print(f.readline(),"\n")
    # print(f.readline(),"\n")