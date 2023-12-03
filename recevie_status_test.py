#Эльвира Зайко, 11 когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request

#запрос на создание нового заказа и проверка статуса
def test_post_new_orders():
    NEW_ORDERS = sender_stand_request.post_new_orders(data.orders_body)
    return NEW_ORDERS

# cохраняем номер трека
def test_save_order_track():
    ORDERS_TRACK = sender_stand_request.post_new_orders(data.orders_body).json()["track"]
    return ORDERS_TRACK


# получение заказа по треку
def test_recevive_response():
    recevive_response = sender_stand_request.get_recevive_otder_response(sender_stand_request.ORDERS_TRACK)
# проверка получения статуса 200 при запросе на получение заказа по треку
    assert recevive_response.status_code == 200,'Failed to get order by track numder'