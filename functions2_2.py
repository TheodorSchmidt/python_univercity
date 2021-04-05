products = []
receipt_num = 1
products_num = 0

def add_item(name, cost):
    '''Добавляет товар в чек.
    
    На вход принимается название товара в формате строки и цена в формате int'''
    global products
    global products_num
    products.append((name, cost))
    products_num += 1

def print_receipt():
    '''Печатает чек'''
    global products
    global products_num
    global receipt_num
    text = []
    receipt_sum = 0
    text.append('Чек ' + str(receipt_num) + '. Всего предметов: ' + str(products_num) + '\n')
    for i in range(len(products)):
        text.append(products[i][0] + ' - ' + str(products[i][1]) + '\n')
        receipt_sum += products[i][1]
    text.append('Итого: ' + str(receipt_sum) + '\n')
    text.append('-----\n')
    products = []
    products_num = 0
    receipt_num += 1
    return text


f_in = open('functions2_2_input.txt', encoding='utf-8')
text = f_in.readlines()
f_in.close()
res_text = ''
f_out = open('functions2_2_output.txt', 'w', encoding='utf-8') 
for i in range(len(text)):
    if text[i].find('print_receipt()') != -1 and products_num > 0:
        f_out.writelines(print_receipt())
    elif text[i].find('add_item(') != -1:
        r = text[i].rfind(')')
        l = text[i].find('(') + 1
        add_data = text[i][l:r].replace("'", "") 
        add_data = add_data.split(', ')
        add_data[1] = int(add_data[1])
        add_item(add_data[0], add_data[1])
f_out.close()