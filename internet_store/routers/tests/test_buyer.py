from fastapi.testclient import TestClient

from  internet_store.main import app

client = TestClient(app)


def test_create_one_buyer():
    params=dict(
        first_name = 'Andrey',
        last_name = 'Grechanik',
        phone = '89999999999',
        email = 'an_grecha@mail.ru',
        password = '1234567890qwerty',
        login = 'angrecha'
    )
    response = client.post(
        "/create",
        json=params)
    
    assert response.status_code == 201
    assert response.json()