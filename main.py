from fastapi import FastAPI, Body, Header
from fastapi.responses import FileResponse, HTMLResponse
import requests_sql as sql
from public.materials import expenses, coming, remains, del_material, balance, remains_all
from public.orders import get_orders_result


app = FastAPI()


@app.get('/')  # main menu
def main_menu():
    return FileResponse("public/index.html")


@app.get('/materials')  # materials menu
def materials_menu():
    return FileResponse("public/materials/index_materials.html")


@app.get('/orders')  # orders menu
def materials_menu():
    return FileResponse("public/orders/index_orders.html")


# materials
@app.get("/expenses")
def expenses_menu():
    return HTMLResponse(expenses.expenses_html(sql.get_list_material()))


@app.get("/coming")
def coming_menu():
    return HTMLResponse(coming.coming_html(sql.get_list_material()))


@app.get("/remain")
def remains_menu():
    return HTMLResponse(remains.remains_html(sql.get_list_material()))


@app.get("/add")
def add_menu():
    return FileResponse("public/materials/add_material.html")


@app.get("/del")
def del_menu():
    return HTMLResponse(del_material.delete_html(sql.get_list_material()))


@app.get("/balance")
def balance_menu():
    return HTMLResponse(balance.balance_html(sql.get_list_material()))


@app.get("/remains_all_result")
def post_remain():
    return HTMLResponse(remains_all.remains_all_html(sql.remains_all_sql()))


# orders
@app.get('/add_order')
def add_order_menu():
    return FileResponse("public/orders/add_order.html")


@app.get('/sum_orders')
def sum_order_menu():
    return FileResponse("public/orders/sum_orders.html")


@app.get('/get_orders')
def get_order_menu():
    return FileResponse("public/orders/get_orders.html")


# post materials
@app.post("/expenses_result")
def post_expenses(data=Body()):
    material_name = data["name"]
    count = data["count"]
    sql.receipts_and_expenditures_add_sql(material_name, 'Расход', count)
    return sql.expenses_sql(material_name, count)


@app.post("/coming_result")
def post_coming(data=Body()):
    material_name = data["name"]
    count = data["count"]
    sql.receipts_and_expenditures_add_sql(material_name, 'Приход', count)
    return sql.coming_sql(material_name, count)


@app.post("/remain_result")
def post_remain(data=Body()):
    material_name = data["name"]
    return sql.remain_sql(material_name)


@app.post("/add_result")
def post_add(data=Body()):
    material_name = data["name"]
    count = data["count"]
    return sql.add_sql(material_name, count)


@app.post("/del_result")
def post_del(data=Body()):
    material_name = data["name"]
    return sql.delete_sql(material_name)


@app.post("/balance_result")
def post_balance(data=Body()):
    material_name = data["name"]
    date1 = data["date1"]
    date2 = data["date2"]
    action = data["action"]
    return sql.receipts_and_expenditures_sql(material_name, action, date1, date2)


# post orders
@app.post('/add_order_result')
def post_add_order(data=Body()):
    order_name = data['name']
    price = data['price']
    date = data['date']
    return sql.orders_add_sql(order_name, price, date)


@app.post('/sum_orders_result')
def post_sum_order(data=Body()):
    date1 = data['date1']
    date2 = data['date2']
    return sql.orders_sum_sql(date1, date2)


@app.get('/get_orders_result')
def post_get_order(data=Header()):
    return get_orders_result.orders_html(sql.orders_get_sql(data))
