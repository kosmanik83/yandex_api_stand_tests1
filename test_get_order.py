#Косыгина Мария 9 когорта — Дипломный проект. Инженер по тестированию плюс
import sender_stand_request

def test_get_order_info_success_response():
    assert sender_stand_request.response_order.status_code == 200
