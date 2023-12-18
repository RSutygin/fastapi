from connect_sql import connect_to_database
from dotenv import load_dotenv
import os
from datetime import date


load_dotenv('config.env')
table = os.getenv('TABLE_SQL')
table_receipts = os.getenv('TABLE_RECEIPTS_SQL')
table_orders = os.getenv('TABLE_ORDERS_SQL')


def expenses_sql(material_name, count):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT lot "
                           f"FROM {table} "
                           f"WHERE name = '{str(material_name)}'")
            count_old = cursor.fetchall()
            count_new = count_old[0][0] - float(count)
            cursor.execute(f"UPDATE {table} SET lot = {count_new} "
                           f"WHERE name = '{str(material_name)}'")
            conn.commit()

        return {"message": f'Материал {material_name} расходован в количестве {count} единиц.\n'
                           f'Остаток: {count_new} единиц'}

    except IndexError:
        return {"message": 'Выберите материал!'}


def get_list_material():
    conn = connect_to_database()
    if conn:
        with conn.cursor() as cursor:
            material_list = ''
            cursor.execute(f"SELECT name "
                           f"FROM {table}")
            temp = cursor.fetchall()
            for i in temp:
                material_list += str(i[0]) + ' '
        conn.close()
        return sorted(material_list.split())

    else:
        return 'Нет соединения, невозможно получить список материалов'


def coming_sql(material_name, count):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT lot "
                           f"FROM {table} "
                           f"WHERE name = '{str(material_name)}'")
            count_old = cursor.fetchall()
            count_new = count_old[0][0] + float(count)
            cursor.execute(f"UPDATE {table} SET lot = {count_new} "
                           f"WHERE name = '{str(material_name)}'")
            conn.commit()

        return {"message": f'Материал {material_name} оприходован в количестве {count} единиц.\n'
                           f'Остаток: {count_new} единиц'}

    except IndexError:
        return {"message": 'Выберите материал!'}


def remain_sql(material_name):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT lot "
                           f"FROM {table} "
                           f"WHERE name = '{str(material_name)}'")
            lot = cursor.fetchall()

        return {"message": f"Остаток материала {material_name} составляет {lot[0][0]} единиц"}

    except IndexError:
        return {"message": 'Выберите материал!'}


def remains_all_sql():  # get all remains
    conn = connect_to_database()
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT name, lot "
                       f"FROM {table} "
                       f"ORDER BY name")
        remain_list = cursor.fetchall()
    conn.close()
    return remain_list


def add_sql(material_name,  count):
    conn = connect_to_database()
    with conn.cursor() as cursor:
        cursor.execute(f"INSERT INTO {table} (name, lot) "
                       f"VALUES ('{str(material_name)}', {float(count)})")
        conn.commit()

    return {"message": f'Материал {material_name} добавлен!'}


def delete_sql(material_name):
    conn = connect_to_database()
    with conn.cursor() as cursor:
        cursor.execute(f"DELETE "
                       f"FROM {table} "
                       f"WHERE name = '{str(material_name)}'")
        conn.commit()

    return {"message": f'Материал {material_name} удален!'}


def receipts_and_expenditures_add_sql(material_name, action, count):
    current_date = date.today()
    conn = connect_to_database()
    with conn.cursor() as cursor:
        cursor.execute(f"INSERT INTO {table_receipts} (material, count, action, day) "
                       f"VALUES ('{str(material_name)}', {float(count)}, '{str(action)}', '{current_date}') ")
        conn.commit()


def receipts_and_expenditures_sql(material_name, action, date1, date2):
    conn = connect_to_database()
    with conn.cursor() as cursor:
        cursor.execute(f"select sum(count) "
                       f"FROM {table_receipts} "
                       f"WHERE material = '{str(material_name)}' AND action = '{str(action)}' AND "
                       f"day BETWEEN '{date1}' AND '{date2}'")
        summa = cursor.fetchall()
    if summa[0][0] is not None:
        return {"message": f'За период с {date1} по {date2} {action.lower()} материала {material_name} '
                           f'равняется {summa[0][0]}'}
    else:
        return {"message": f'За период с {date1} по {date2} {action.lower()} материала {material_name} '
                           f'не производился'}


def orders_add_sql(order_name, price, order_day):
    conn = connect_to_database()
    with conn.cursor() as cursor:
        cursor.execute(f"INSERT INTO {table_orders} (order_name, price, day) "
                       f"VALUES ('{str(order_name)}', {float(price)}, '{order_day}') ")
        conn.commit()

    return {"message": f'Заказ ценой {price} добавлен!'}


def orders_sum_sql(date1, date2):
    conn = connect_to_database()
    with conn.cursor() as cursor:
        cursor.execute(f"select sum(price) "
                       f"FROM {table_orders} "
                       f"WHERE day BETWEEN '{date1}' AND '{date2}'")
        summa = cursor.fetchall()
    if summa[0][0] is not None:
        return {"message": f'За период с {date1} по {date2} сумма заказов составляет {summa[0][0]}'}
    else:
        return {"message": f'За период с {date1} по {date2} заказов нет.'}


def orders_get_sql(date1):
    conn = connect_to_database()
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT order_name, price "
                       f"FROM {table_orders} "
                       f"WHERE day = '{date1}'"
                       f"ORDER BY day")
        order_list = cursor.fetchall()
    return order_list
