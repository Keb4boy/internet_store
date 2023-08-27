from fastapi.testclient import TestClient
from internet_store.main import app
from internet_store.models import Buyer
from sqlalchemy.future import select


#тест для router.post('/create')

# def test_add_buyer():
#     client = TestClient(app)
#     buyer_data = {
#         "first_name": "John",
#         "last_name": "Doe",
#         "phone": "123456789",
#         "email": "johndoe@example.com",
#         "password": "password123",
#         "login": "johndoe"
#     }
#     response = client.post(f"/buyer/create", json=buyer_data)
#     assert response.status_code == 200
#     assert response.json() == buyer_data


# тест для router.get('/{buyer_id}')

def test_get_buyer():
    client = TestClient(app)
    buyer_data = {
        "first_name": "John",
        "last_name": "Doe",
        "phone": "123456789",
        "email": "johndoe@example.com",
        "password": "password123",
        "login": "johndoe"
    }
    # перед тестом добавляем покупателя в базу данных
    response = client.post(f"/buyer/create", json=buyer_data)

    print(response.json())
    # получаем ID добавленного покупателя из ответа добавления
    buyer_id = Buyer.select("id").where(Buyer.email == "johndoe@example.com")

    
    # делаем запрос на получение покупателя по ID
    response = client.get(f"/buyer/{buyer_id}")

    assert response.status_code == 200
    assert response.json() == buyer_data