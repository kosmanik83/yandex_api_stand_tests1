#Косыгина Мария 9 когорта — Дипломный проект. Инженер по тестированию плюс
import configuration
import requests
import data

#Создаю новый заказ
def post_new_orders(body):
    return requests.post(configuration.URL_SERVER + configuration.CREATE_ORDERS,
                         json=body)

#Сохраняю номер трека заказа
def get_new_track():
    order_responce = post_new_orders(data.order_body)
    track = str(order_responce.json()["track"])
    return track

#Выполняю запрос на получения заказа по треку заказа.
def get_order():
     return requests.get(configuration.URL_SERVER + configuration.GET_ORDERS +"t?=")
response_order = get_order()
