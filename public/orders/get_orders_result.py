def orders_html(orders_list):
    result = ''
    for order in orders_list:
        result += f'''Заказ: {str(order[0])}; цена: {str(order[1])} рублей<br>'''
    return result
