import requests
import configuration
import data

#создание нового заказа
def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body)


#сохранение номера трека заказа
ORDERS_TRACK = post_new_orders(data.orders_body).json()["track"]


#получение заказа по треку
def get_recevive_otder_response(track):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDERS_TRACK + str(track))
