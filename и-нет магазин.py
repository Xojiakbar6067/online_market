sklad={'склад':{}}
karzina={}
while True:
    print('--------------------''\n''1-пополнит склад','\n''2-покозат товари в складе','\n''3-добавит в карзину','\n''4-покозат корзину')
    operator=int(input('выбирайте команду: '))
    if operator==1:
        produkt_name=input('названия продукта: ')
        produkt_count=int(input('количество продукта: '))
        sklad['склад'][produkt_name]=produkt_count
        print(f'{produkt_count}кг {produkt_name} добавлен в склад')

    elif operator==2:
        k=0
        for i, j in sklad['склад'].items():
            k+=1
            print(f'{k}) {i}____{j}кг')
    elif operator==3:
        produkt_name_buy = input('названия продукта: ')
        produkt_count_buy = int(input('количество продукта: '))
        if produkt_name_buy in karzina.keys():
            karzina[produkt_name_buy]+=produkt_count_buy
        else:
            karzina[produkt_name_buy]=produkt_count_buy
        sklad['склад'][produkt_name_buy]-=produkt_count_buy
        print(f'{produkt_count_buy}кг {produkt_name_buy} добавлен в корзину')
    elif operator==4:
        k=0
        for i, j in karzina.items():
            k+=1
            print(f'{k}) {i}____{j}кг')
    else:
        print('было указано не правилный команда')